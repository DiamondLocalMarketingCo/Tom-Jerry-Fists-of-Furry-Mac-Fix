# Tom and Jerry in Fists of Furry - Mac CrossOver Fix

This is a compatibility fix I made for the Windows PC version of **Tom and Jerry in Fists of Furry** so it can run properly on an Apple Silicon Mac through CrossOver.

The original game would crash during startup. After getting it running, the intro and menus also had fullscreen problems. This fix gets the game running and keeps the intro, menus, and matches fullscreen.

I tested it on a **MacBook Air M2** with **CrossOver 26.3.0**.

## How to use

1. Install the Windows PC version of the game in CrossOver.
2. Download `make-fixed-exe.py` from this repository and put it next to your `TJPC (release).exe`.
3. Open Terminal in that folder and run:
   ```bash
   python3 make-fixed-exe.py
   ```
4. It will create `TJPC-CrossOver-M2-Final.exe`.
5. In CrossOver, use **Run Command** and select the new EXE.
6. Use **Full screen**, **DirectDraw HAL - Direct3D HAL**, and **32-bit rendering** in the game settings.
7. Leave CrossOver **Graphics** on **Auto** and **High Resolution Mode** off.

You still need your own copy of the game. This is not a native macOS port, just a compatibility fix for running the original PC version through CrossOver.

This repository is mainly a small portfolio/demo project documenting the fix.
