---
title: "The New SDLC With Vibe Coding"
description: "Exploring Google's whitepaper on vibe coding vs agentic engineering"
date: "2026-07-02"
tags:
  - "AI"
  - "coding"
  - "software development"
---

I'm very excited to play through the ideas in [Google's whitepaper on The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding) and attempt to apply them to both my $200/year Claude subscription and some offline AI running on an M4 with 24GB of RAM.

The whitepaper, authored by Addy Osmani, Shubham Saboo, and Sokratis Kartakis, draws an important distinction between two approaches:

- **Vibe Coding**: Describe what you want in natural language, accept the AI's output, and when something breaks, paste the error back and ask the AI to fix it.

- **Agentic Engineering**: AI handles implementation within a carefully designed system of constraints, tests, and feedback loops, with humans retaining oversight over architecture and quality.

The key insight is that vibe coding works fine for prototypes, but can quietly cause problems in production systems. Verification is what determines where you land on the spectrum between these two approaches, and the right spot depends on the stakes.
