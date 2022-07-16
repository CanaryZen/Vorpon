# (c) Advanche Corporation. All rights reserved.
# Vorpon
A Python-Based Gaming Console using the VPG-PY Architecture (Vorpon Processor Graphics-Python).

# About Vorpon
Vorpon is a Python-Based Gaming Console using the VPG-PY Architecture (Vorpon Processor Graphics-Python) and is meant to look similar to the Original Nintendo Game Boy. But instead of using the Sharp LR35902 core processor, it uses a Virtual Processor/Architecture which is based off the x86-64/ARM64 Processors/Architectures. Vorpon also comes with it's own BIOS (Basic Input/Output System) which is used to verify The Configuration/Games, making sure that The Configuration/Games is not either deleted or corrupted.

Unlike the Original Nintendo Game Boy, the Advanche Vorpon runs on a Dual-Band Virtual Processor which lets the BIOS do some tests on both the BIOS Configuration, and the game itself. Making sure if the BIOS Configuration/Game is not either deleted or corrupted.

# Modding Vorpon
Vorpon is also open source, which makes you able to customize your own Vorpon to your needs. You can also make mods for the Vorpon, just take note that any errors that happen between the Custom Games/Applications made by users and Officially Verified Games for Vorpon will lead to a Corruption error when trying to launch the Game/3rd-Party Application. Rendering the Custom Game/Application unusable unless fixed. Of course you can bypass this corruption error by deleting the corruption detection, but make sure that if you remove subprocess completely, Vorpon will bootloop. Though this isn't seen a lot just take note about that.

# 🐞 Vulnerabilities/Stability
**Vulnerabilities/Stability:**
|               Vulnerabilities              |         Stability               |
| ------------------------------------------ | ------------------------------- |
| False BIOS/Configuration Errors (Ctrl+C)   | ✅ Doesn't Corrupt/Crash Vorpon |

# Python Versions
**Codenames:**
| Codenames     | Versions       | Python Versions           |
| ------------- | -------------- | ------------------------- | 
| Vortex        | 0.4.50674-dev  | ✅ Python 3.5.9 - Latest |
| Vortex        | 0.7.80639-dev  | ✅ Python 3.5.9 - Latest |
| Vortex        | 0.9.14096-dev  | ✅ Python 3.5.9 - Latest |
| Vortex        | 1.0.20491.8240 | ✅ Python 3.5.9 - Latest |

# Optional Requirements (For Certain Games)
| Requirements    | Stability          |
| --------------- | ------------------ |
| Pygame          | ✅ Works           |
| Vorpon Game Pak | 🔨 In Development  |
