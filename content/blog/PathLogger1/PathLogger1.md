---
title: "Path Logger, Version 1"
description: "A small Firebase app for logging simplex contacts and mapping the path between stations"
date: "2026-07-18"
tags:
  - "logs"
  - "simplex"
  - "coding"
  - "Firebase"
---

Simplex is where the interesting radio happens. No repeater, no linked system, just two stations and whatever the terrain and the antennas will allow. The part I kept wanting to keep track of was not the contact itself but the *path* — where I was, where the other station was, and whether that path worked again later.

So I built Path Logger. Version 1 is deliberately small.

## What it does

- **Logs the contact.** Callsign, date and time, frequency, mode, and signal reports, typed in on the spot.
- **Captures location.** The browser's geolocation gives me my position, and I record the other station's grid or coordinates. That turns a log entry into two endpoints instead of one.
- **Maps the path.** Every logged contact draws a line between the two stations, so a night of simplex work becomes a picture of what actually got out.
- **Shares the log.** Multiple operators can sign in to the same project and see each other's entries. During a net or a group activation, everyone's contacts land in one map.

## Why Firebase

I wanted to spend my time on the logging, not on hosting. The free tier covers everything version 1 needs: Firestore for the contact records, Authentication so operators sign in rather than sharing a password, and Hosting to serve the whole thing. No server to patch, no database to back up by hand, and the app is a URL I can open on a phone in the truck.

The tradeoff is honest: this is somebody else's platform and somebody else's quota. For a hobby log of simplex contacts, that's a trade I'm happy to make. If it outgrows the free tier, exporting Firestore documents to something self-hosted is not a hard problem.

## What version 1 is not

It is not a general-purpose logger. There is no ADIF import, no LoTW or QRZ integration, no contest support. If you want a real log, use a real logger. Path Logger exists to answer one question: what paths have worked, from where, on simplex?

Version 2 ideas, roughly in order of how much I want them: ADIF export, elevation profile along the path, and marking a contact as a repeat so I can see which paths are reliable versus lucky.

The demo is live — try it and tell me what's missing.
