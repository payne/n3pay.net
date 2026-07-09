# Claude Code Interaction Log

This file is automatically maintained by Claude Code hooks.

---

# Session Started [2026-02-26 06:53:48]

Session ID: `339ee5f3...`

---

# Session Ended [2026-02-26 13:52:54]

---

# Session [2026-07-08]

## Request
Move the blog to `/blog/` and turn the site root into a landing page listing
applications, driven by `app-menu.json`. Table needs sortable columns, a filter,
a column-visibility widget, default sort ascending by title, default columns
title + last-updated, and a first-column Launch button opening each app in a new
window.

## Decisions (from the user)
- Blog served at `https://n3pay.net/blog/` (a path), not a `blog.` subdomain.
- Landing page built through Eleventy, reusing `base.njk` layout/CSS + theme toggle.
- The blog `app-menu.json` entry points at `/blog/` (since the blog now lives there).

## Changes
- `public/app-menu.json` — new single source for the app list (served at
  `/app-menu.json`).
- `_data/appMenu.js` — reads `public/app-menu.json` at build time so the table is
  also server-rendered (no-JS fallback).
- `content/index.njk` — rewritten as the landing page: server-rendered `<noscript>`
  list + embedded JSON (`<script … id="app-menu-data" eleventy:ignore>`) + bundled
  CSS/JS that builds the interactive sortable/filterable table with a column widget.
  Default sort title asc; default columns Launch + Title + Last updated.
- `content/blog.njk` — repurposed into the blog home (former root `index.njk`
  content: intro, links, latest 20 posts, Mastodon), now at `/blog/`; PicoFOX image
  paths made absolute (`/blog/PicoFOX/…`), archive link points to `/blog/archive/`.
- `content/archive.njk` — new full post archive at `/blog/archive/`.
- `eleventy.config.js` — watch `public/app-menu.json` for dev rebuilds.

## Gotcha
The bundle plugin's `bundleHtmlContentFromSelector: "script"` swept the embedded
JSON `<script>` into the JS bundle (stripping it from the HTML). Fixed by adding
`eleventy:ignore` to that one script tag.

## Verification
`npm run build` clean. Headless Chrome render confirms: default columns
Launch/Title/Last-updated, sort title-ascending, 3 Launch buttons, filter +
columns widgets present. Node tests confirm date sort (missing date sorts last in
both directions) and filter across all fields. Routes `/`, `/blog/`,
`/blog/archive/`, `/app-menu.json` all 200; blog home shows 20 latest posts,
archive shows all.

---

