"""Render content/*.md into a single static index.html.

Usage: uv run build.py
"""

import sys
from datetime import date
from html import escape
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]

INTRO_REQUIRED = ["name", "tagline", "photo", "site_url", "github"]
PROJECT_REQUIRED = ["title", "summary"]


def load(path: Path, required: list[str]) -> tuple[dict, str]:
    """Split a markdown file into (frontmatter dict, body markdown)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        sys.exit(f"{path.name}: missing frontmatter (file must start with '---')")
    try:
        _, front, body = text.split("---", 2)
    except ValueError:
        sys.exit(f"{path.name}: frontmatter is not closed with a second '---'")
    meta = yaml.safe_load(front) or {}
    missing = [key for key in required if not meta.get(key)]
    if missing:
        sys.exit(f"{path.name}: missing required field(s): {', '.join(missing)}")
    return meta, body.strip()


def to_html(body: str) -> str:
    return markdown.markdown(body, extensions=MD_EXTENSIONS)


def link(label: str, url: str) -> str:
    return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'


def render_intro_links(intro: dict) -> str:
    items = [("GitHub", intro["github"])]
    if intro.get("linkedin"):
        items.append(("LinkedIn", intro["linkedin"]))
    if intro.get("email"):
        items.append(("Email", f"mailto:{intro['email']}"))
    return "".join(f"<li>{link(label, url)}</li>" for label, url in items)


def render_card(meta: dict, body: str) -> str:
    parts = ['        <article class="card">']

    if meta.get("image"):
        parts.append(
            f'          <img class="card-image" src="{escape(meta["image"], quote=True)}" '
            f'alt="{escape(meta["title"])} thumbnail" loading="lazy">'
        )

    parts.append('          <div class="card-body">')
    parts.append(f"            <h3>{escape(meta['title'])}</h3>")

    meta_line = " · ".join(str(meta[k]) for k in ("role", "period") if meta.get(k))
    if meta_line:
        parts.append(f'            <p class="meta">{escape(meta_line)}</p>')

    parts.append(f'            <p class="summary">{escape(meta["summary"])}</p>')

    if meta.get("tags"):
        tags = "".join(f"<li>{escape(str(t))}</li>" for t in meta["tags"])
        parts.append(f'            <ul class="tags">{tags}</ul>')

    if meta.get("links"):
        links = "".join(link(item["label"], item["url"]) for item in meta["links"])
        parts.append(f'            <div class="card-links">{links}</div>')

    if body:
        parts.append(
            "            <details>\n"
            "              <summary>Read more</summary>\n"
            f'              <div class="details-body">{to_html(body)}</div>\n'
            "            </details>"
        )

    parts.append("          </div>")
    parts.append("        </article>")
    return "\n".join(parts)


def render_cards(dir_path: Path) -> list[str]:
    """Render every .md file in dir_path as a card, sorted by filename."""
    files = sorted(dir_path.glob("*.md"))
    return [render_card(*load(p, PROJECT_REQUIRED)) for p in files]


def wrap_section(cards: list[str], heading: str, css_class: str) -> str:
    """Wrap rendered cards in a '<section>'. Returns "" if there are no cards,
    so an empty section (e.g. no WIP projects yet) is omitted from the page."""
    if not cards:
        return ""
    return (
        f'    <section class="{css_class}">\n'
        f"      <h2>{escape(heading)}</h2>\n"
        f'      <div class="grid">\n'
        f"{chr(10).join(cards)}\n"
        f"      </div>\n"
        f"    </section>"
    )


def main() -> None:
    intro, bio = load(CONTENT / "intro.md", INTRO_REQUIRED)

    project_cards = render_cards(CONTENT / "projects")
    if not project_cards:
        sys.exit("No project files found in content/projects/")

    wip_cards = render_cards(CONTENT / "wip")

    site_url = intro["site_url"].rstrip("/")
    values = {
        "name": escape(intro["name"]),
        "tagline": escape(intro["tagline"], quote=True),
        "photo": escape(intro["photo"], quote=True),
        "site_url": escape(site_url, quote=True),
        "bio": to_html(bio),
        "intro_links": render_intro_links(intro),
        "projects": "\n".join(project_cards),
        "wip_section": wrap_section(wip_cards, "Works in Progress", "wip"),
        "year": str(date.today().year),
    }

    html = (ROOT / "template.html").read_text(encoding="utf-8")
    for key, value in values.items():
        html = html.replace("{{" + key + "}}", value)

    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Built index.html ({len(project_cards)} project(s), {len(wip_cards)} WIP)")


if __name__ == "__main__":
    main()
