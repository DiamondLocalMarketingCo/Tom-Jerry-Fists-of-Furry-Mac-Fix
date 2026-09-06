# Tom and Jerry in Fists of Furry - Mac CrossOver Fix

This is a compatibility fix I made for the Windows PC version of **Tom and Jerry in Fists of Furry** so it can run properly on an Apple Silicon Mac through CrossOver.

The original game would crash during startup, and after getting it running the intro and menus also had fullscreen issues. This build fixes the startup problem and keeps the intro, menus, and matches fullscreen.

I tested this on a **MacBook Air M2** with **CrossOver 26.3.0**.

## How to use

1. Install the Windows PC version of the game in CrossOver.
2. Download `TJPC-CrossOver-M2-Final.exe` from this repository.
3. Put it in the main game folder next to the original game executable.
4. In CrossOver, use **Run Command** and select `TJPC-CrossOver-M2-Final.exe`.
5. Use these game settings:
   - Full screen
   - DirectDraw HAL - Direct3D HAL
   - 32-bit rendering
6. In CrossOver, leave **Graphics** on **Auto** and **High Resolution Mode** off.

You still need your own installed copy of the game. This is not a native macOS port, just a compatibility fix for running the original PC version through CrossOver.

This repository is mainly a small portfolio/demo project documenting the fix.
