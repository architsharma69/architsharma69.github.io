---
title: Personal OneNote preview service
role: Creator
period: 2026 July - Present
summary: A simple, locally-hosted utility meant to streamline the process of previewing and saving my OneNote pages as PDFs
tags: [Python, Applescript, UI Design, Automation]
image: assets/OneNote.jpeg 
links:                                  # optional
  - label: Link to the GitHub repository
    url: https://github.com/architsharma69/OneNote_Paginate_Utility
---

## The Issue
OneNote is designed as an endless page - it does not automatically create pagebreaks when writing notes. It also doesn't display guidelines to indicate where the page will be split when the document is exported. For someone that uses OneNote to write assignments, I needed to know how the pages will be split when I exported my document as a PDF.

## What I did
- Created a utility script that displays a preview of the PDF on a scalable `tkinter` window.
- Used Applescripts along with MacOS `Shortcuts` to trigger the service using keyboard shortcuts