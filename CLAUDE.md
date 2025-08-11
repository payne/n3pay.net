# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Eleventy-based static site blog built from the eleventy-base-blog v9 starter template. It uses Eleventy v3 with zero-JavaScript output for optimal performance.

## Core Architecture

- **Static Site Generator**: Eleventy v3 with ES modules
- **Input Directory**: `content/` - all content files live here
- **Output Directory**: `_site/` - generated static files
- **Template Engine**: Nunjucks (for .html and .md files)
- **Content Structure**:
  - Blog posts: `content/blog/` with `posts` tag
  - Pages: `content/` (index, about, 404, etc.)
  - Data: `_data/` directory with global site data
  - Templates: `_includes/layouts/` (base, home, post)
  - Static assets: `public/` copied to output root

## Development Commands

- **Start development server**: `npm start` or `npx @11ty/eleventy --serve --quiet`
- **Build for production**: `npm run build` or `npx @11ty/eleventy`
- **Debug build**: `npm run debug` (shows Eleventy internals)
- **Debug with server**: `npm run debugstart`
- **Performance benchmark**: `npm run benchmark`

## Key Configuration Files

- `eleventy.config.js`: Main Eleventy configuration with plugins and build settings
- `_data/metadata.js`: Global site metadata (title, URL, author info)
- `_config/filters.js`: Custom Eleventy filters for date formatting and data manipulation

## Content Management

- **Drafts**: Use `draft: true` in front matter - visible in development, excluded from production builds
- **Navigation**: Use `eleventyNavigation` key in front matter for site navigation
- **Tags**: Blog posts use tags for categorization, automatically generates tag pages
- **Images**: Automatic optimization with multiple formats (AVIF, WebP, fallback)

## Template Structure

- **Base Layout**: `_includes/layouts/base.njk` - HTML structure
- **Home Layout**: `_includes/layouts/home.njk` - homepage template  
- **Post Layout**: `_includes/layouts/post.njk` - blog post template
- **Post List Component**: `_includes/postslist.njk` - reusable post listing

## Asset Pipeline

- CSS and JS bundling via `eleventy-plugin-bundle`
- Image optimization with `@11ty/eleventy-img`
- Syntax highlighting with PrismJS
- RSS/Atom feed generation

## Deployment

- Supports GitHub Pages, Netlify, Vercel, Cloudflare Pages
- Configuration files: `netlify.toml`, `vercel.json`
- Use `npm run build-ghpages` for GitHub Pages with path prefix