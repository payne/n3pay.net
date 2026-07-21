---
title: "QUANSHENG UV-K5"
description: "Getting into custom firmware and digital modes with the UV-K5 version 3"
date: "2026-07-21"
tags:
  - "QUANSHENG"
  - "UV-K5"
  - "HT"
  - "firmware"
  - "digital"
---

Aaron's talk about custom firmware inspired me to get a pair of UV-K5 version 3 radios and some AIOCs. Hoping to have fun learning digital modes at my QTH.


Here's a long google AI response to the search "quansheng uv-k5 digipi aioc"

Combining the Quansheng UV-K5, an AIOC (All-In-One Cable), and a DigiPi creates a powerful, budget-friendly portable digital amateur radio hotspot. The AIOC functions as a USB soundcard, serial adapter, and PTT controller, bridging the UV-K5 to the Raspberry Pi running DigiPi. [1, 2, 3, 4]

### The Components

1. Quansheng UV-K5: An incredibly versatile and inexpensive handheld transceiver (HT) covering VHF/UHF and airband, which can be modified via custom firmware.
1. AIOC: An open-source interface board (also known as "Universal Radio Controller") that connects to the radio's dual-pin K1 port on one end and the DigiPi via a single USB-C cable on the other. It handles both audio and PTT flawlessly.
1. DigiPi: A project and specialized operating system for the Raspberry Pi (built by KM6LYW) that gives you a web-based portal to run data modes like APRS, Winlink, JS8Call, and FLdigi right from your phone or browser. [3, 12]

### How to Set It Up

1. Radio Settings: On the Quansheng, set the volume to around 25% and ensure you have the correct squelch settings configured for digital data.
2. AIOC to DigiPi: Connect the AIOC’s twin-prong connector to the radio. Connect the AIOC to the DigiPi’s USB port.
3. Initialize DigiPi: Boot up your DigiPi and navigate to the web interface. On the Initialization page, choose your AIOC (typically listed as ) as the radio interface. Enter your callsign, grid square, and APRS settings.
4. Firmware (Optional): Many users flash custom firmware (like IJV or DOCK firmware) to the UV-K5 to unlock better performance, like 'flat audio' or direct rig control. [19, 20, 21, 22]

### Potential Challenges to Watch For

1. RF Interference (RFI): Because everything is highly portable, your HT's transmitted signal can easily feed back into the Raspberry Pi or the AIOC, causing the radio to get stuck in "transmit" mode.
1. Fix: Users in the DigiPi forums recommend adding ferrite beads on both ends of your USB cable and physically keeping the radio's antenna at least 2 meters away from the DigiPi board.
1. Audio Levels: Because HTs aren't strictly designed for continuous-duty digital data, you may need to fine-tune your audio input/output levels using the DigiPi web menu so your signal isn't over-deviated. [3, 24]

If you're building this setup, could you tell me which version of the Raspberry Pi you are using and which digital modes (like APRS, JS8Call, or Winlink) you plan to use? I can help you with your specific configuration files!

AI responses may include mistakes.

### References

1. [YouTube: APRS for the Quansheng UV-K5! Utilizing The AIOC / All in One Cable](https://www.youtube.com/watch?v=nOHxzZ19w7A)
2. [g1lro.uk — DigiPi build notes](https://g1lro.uk/?p=85)
3. [Patreon — DigiPi 1.9.3 on Raspberry Pi](https://www.patreon.com/posts/digipi-1-9-3-on-123412689)
4. [craiger.org — DigiPi](https://craiger.org/digipi/)
5. [Amazon — Quansheng UV-K5 handheld](https://www.amazon.com/QUANSHENG-UV-K5-Handheld-Rechargeable-Survival/dp/B0CB8XXBH4)
6. [hamimports.com — Quansheng UV-K5](https://hamimports.com/radio/quansheng-uv-k5/)
7. [baofengradio.co.uk — Quansheng UV-K5 multi-band radio](https://baofengradio.co.uk/quansheng-uv-k5-multi-band-radio/)
8. [r/Quansheng — APRS with the UV-K5/8: best option](https://www.reddit.com/r/Quansheng/comments/1ko1v9w/aprs_with_the_uvk58_what_is_the_best_option/)
9. [YouTube: AIOC - AUDIO & MICROPHONE SET UP - QUANSHENG DOCK](https://www.youtube.com/watch?v=hO8kx_4WTUw)
10. [YouTube: LEARNING - AIOC -Universal Radio Controller - & DigiPi Under development](https://www.youtube.com/watch?v=rDNKQlGhIrY)
11. [Google Groups — DigiPi](https://groups.google.com/g/digipi/c/1NfZeLpsT4M)
12. [Facebook — HamOps group post](https://www.facebook.com/groups/hamops/posts/10163083506498840/)
13. [Google Groups — DigiPi](https://groups.google.com/g/digipi/c/LybQBGjJ37A)
14. [YouTube: Quansheng UV-K5 - Upload Firmware -AIOC Universal Radio Controller Box](https://www.youtube.com/watch?v=tTx79CtOu_4)
15. [YouTube: Easy & Effective APRS: Using the TOADS Digital Interface & AIOC with DigiPi for a Digipeater & iGate](https://www.youtube.com/watch?v=m1qb0s_MuMo)
16. [YouTube: Every Radio Data Mode on Your Phone!](https://www.youtube.com/watch?v=6KAeJyEz8I8)
17. [g1lro.uk — UV-K5 notes](https://g1lro.uk/?p=63)
18. [YouTube: Amateur Radio DATA HotSpot! Operate with Your Phone! Build & Demo.](https://www.youtube.com/watch?v=lB1puo2FwwU)
19. [YouTube: Quansheng UV-K5 - Upload Firmware -AIOC Universal Radio Controller Box](https://www.youtube.com/watch?v=tTx79CtOu_4)
20. [YouTube: Quansheng UV-K5/K6 on M17, DMR, NXDN,... Flat Audio Mod](https://www.youtube.com/watch?v=oMhtGjtORUk)
21. [hampager.de — UV-K5 wiki](https://hampager.de/dokuwiki/doku.php?id=uvk5)
22. [YouTube: QUANSHENG UV-K5 weak CW/SSB signals improvement ( IJV 2.9 firmware )](https://www.youtube.com/watch?v=xuUrVQIeFrU)
23. [Google Groups — DigiPi](https://groups.google.com/g/digipi/c/wj50P_zgPR0)
24. [YouTube: Every Radio Data Mode on Your Phone!](https://www.youtube.com/watch?v=6KAeJyEz8I8)
