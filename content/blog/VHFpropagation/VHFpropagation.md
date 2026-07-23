---
title: "How does VHF propagation get measured?"
description: "A live VHF propagation map from APRS packets — thanks to Jim KX0U for the pointer"
date: "2026-07-23"
tags:
  - "web"
  - "VHF"
  - "tools"
  - "APRS"
  - "propagation"
---

Thanks to Jim KX0U for showing me [vhf.dxview.org](https://vhf.dxview.org/map?center=40.35,-95.23,7.0). It's a live map that colors the country by how far VHF signals are getting out right now — greens and yellows where things are normal, oranges and reds where the band is open. That's a great picture, but it left me wondering: where does that data actually come from? Nobody is out there with a signal generator sweeping the whole country every hour.

## The trick: use the traffic that's already there

The [VHF map](https://vhf.dxview.org/) doesn't run its own beacons. Instead it listens to a network that's already broadcasting all day long — [APRS](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System), the Automatic Packet Reporting System.

APRS stations sit on 144.390 MHz (here in North America) and send short packets: position beacons, weather data, messages, and digipeater IDs. Thousands of them are transmitting around the clock. Every one of those packets is a tiny, timestamped, geolocated propagation test that somebody already paid for.

## How a packet becomes a data point

Here's the chain:

1. **A station transmits a packet.** It contains the sender's callsign and, usually, its position (or a known fixed location).
2. **Another station hears it and gates it to the internet.** These are [I-gates](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System) (Internet gateways). When an I-gate copies a packet off the air, it forwards it to **APRS-IS**, the internet backbone of the APRS network, and stamps it with *its own* callsign and location.
3. **Now you have two endpoints.** The packet knows where it came from (the sender) and where it was received (the I-gate). Both have known coordinates.

That's the whole measurement. A packet that traveled from station A to I-gate B, received in the last hour, means 2 meters supported at least that A-to-B distance at that moment. Most hops are short and local. But when the band opens — tropospheric ducting, a temperature inversion, sporadic-E — I-gates start hearing stations from hundreds of miles away, and those long paths light up.

## From dots to a footprint

The map takes all those received paths from the past hour and smooths them into a color-coded footprint. If the longest paths being copied in your area are 50 miles, you're green. If I-gates near you are suddenly pulling in packets from 300 miles out, that region goes orange to red. It's not predicting propagation from solar numbers or a model — it's showing you what *actually got through*, reverse-engineered from ordinary APRS traffic.

## Why this is clever

The same idea powers a lot of ham propagation tools, but with different source data:

- The **HF sibling** at [hf.dxview.org](https://hf.dxview.org/) leans on the [Reverse Beacon Network](https://www.reversebeacon.net/) (automated CW and FT8 skimmers) and [PSK Reporter](https://pskreporter.info/) instead of APRS.
- [PSK Reporter](https://pskreporter.info/) does the same trick for FT8/digital modes: every decoded signal is a spot with two known endpoints.

In each case the insight is the same — you don't need a dedicated beacon network if you're willing to treat the everyday traffic as your beacons. On VHF, APRS packets are perfect for it: short, frequent, geolocated, and already flooding the internet through I-gates.

So the next time your position beacon gets gated by a station three states away, you weren't just showing off — you were a data point telling everyone the band was open.

## Sources

- [VHF Real Time Propagation — vhf.dxview.org](https://vhf.dxview.org/)
- [HF+ Real Time Propagation — hf.dxview.org](https://hf.dxview.org/)
- [PSK Reporter](https://pskreporter.info/)
- [Reverse Beacon Network](https://www.reversebeacon.net/)
- [APRS on Wikipedia](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System)
