---
title: FormDraft
role: Creator
period: 2026 - Present
summary: A browser extension that scans online forms, saves them as editable local drafts, and pastes everything back in one step.
tags: [Chrome Extension, JavaScript, React]
image: assets/formdraft.jpeg   # optional; delete this line for a card with no thumbnail
---

## Description
Many online forms don't persist your responses between sessions — you leave and come back to a blank form, dropdowns and all. FormDraft treats any web form like a document: capture it once, draft your answers locally, and fill it back in with one click.

## What I'm building
- **Scan** — a two-pass capture. A DOM parser handles native `<input>`, `<select>` and `<textarea>` fields first; a screenshot + Claude vision fallback catches whatever it misses (custom div-based dropdowns, styled radio groups) and merges the results into one JSON template.
- **Draft** — the extension popup renders the saved template as an editable form, with multiple drafts supported per URL (e.g. several job applications on the same portal).
- **Fill** — native fields are refilled via synthetic `input`/`change` events, so React/Vue/Angular apps register the change in their own state, not just the DOM. Custom UI fields are located and clicked using the LLM's description of the element. Fields that genuinely can't be automated — CAPTCHAs, signature pads — are flagged for manual completion instead of guessed at.

## Tech stack
Chrome Extension (Manifest V3), vanilla JS content scripts, React + Vite popup UI, `chrome.storage.local` for persistence, Claude API for the vision fallback.

## Current scope
Custom UI components and multi-page or branching forms are best-effort in v1. CAPTCHAs are intentionally out of scope.
