# Portfolio website

A single static page generated from markdown. Live at https://architsharma69.github.io

## Editing content

| To change...        | Edit                                   |
| ------------------- | -------------------------------------- |
| Name, bio, links    | `content/intro.md`                     |
| Profile photo       | replace `assets/profile.svg` (or point `photo:` in `intro.md` at a new `.jpg`/`.png`) |
| A project           | `content/projects/<file>.md`           |
| Add a project       | new `.md` in `content/projects/`       |
| Reorder projects    | rename files — they sort by filename (`01-…`, `02-…`) |
| Look and feel       | `style.css` (colours are variables at the top) |

Project frontmatter fields: `title` and `summary` are required; `role`, `period`, `tags`,
`image` and `links` are optional. Everything below the frontmatter is the full write-up,
shown under "Read more". Put images in `assets/` and reference them as `assets/name.png`.

## Build and preview

```sh
uv run build.py                 # regenerates index.html
python3 -m http.server          # then open http://localhost:8000
```

`uv run` creates the virtualenv and installs dependencies from `pyproject.toml` / `uv.lock`
on first use. `index.html` is generated, but it is committed: GitHub Pages serves it as-is.

## Deploy (GitHub Pages)

One-time setup:

1. On GitHub, create a **public** repo named exactly `architsharma69.github.io`
   (no README, no .gitignore — this repo already has them).
2. In this folder:
   ```sh
   git init -b main
   git add .
   git commit -m "Initial portfolio site"
   git remote add origin https://github.com/architsharma69/architsharma69.github.io.git
   git push -u origin main
   ```
3. Repo **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*,
   Branch = `main`, folder = `/ (root)`. The site is live in about a minute.

Every update after that:

```sh
uv run build.py
git add . && git commit -m "Update content" && git push
```

Remember to run the build before committing, or the live site won't change.
