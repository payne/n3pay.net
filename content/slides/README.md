---
permalink: false
---
# Slides Directory Structure

This directory contains individual presentation pages.

## Structure

```
content/slides/
├── README.md (this file - not published)
├── presentation-name.md (individual presentation page)
└── another-presentation.md

public/slides/
├── presentation-name/
│   ├── image1.png
│   ├── image2.jpg
│   └── diagram.svg
└── another-presentation/
    └── photos.jpg
```

## Creating a New Presentation

1. Create a new `.md` file in `content/slides/` (e.g., `my-talk.md`)
2. Add front matter with title, description, and date
3. Write your presentation content using Markdown
4. Create a folder in `public/slides/` with the same name (e.g., `public/slides/my-talk/`)
5. Place all images for that presentation in the folder
6. Reference images in your markdown: `![Alt text](/slides/my-talk/image.png)`
7. Update `content/slides.md` to link to your new presentation: `[My Talk](/slides/my-talk/)`

## Example Front Matter

```yaml
---
title: My Presentation Title
description: Brief description of the talk
date: 2026-01-09
---
```

## Notes

- The `permalink: false` in this README's front matter prevents it from being published
- Images in `public/slides/` are copied to `_site/slides/` during build
- Each presentation gets its own URL: `/slides/presentation-name/`
