# SpedaTex Tool

This repository contains a GUI-based tool (SpedaTex.py) for converting .png files to .dds files and optionally packaging them into .texture files using SilkTexture. Tailored for Marvel's Spider-Man 2 PC

## Features
- Batch conversion of PNG images to DDS via NVIDIA Texture Tools (nvtt_export).
- BC7/BC1 formats for color and gloss textures, with BC5 for normal maps.
- Automated .texture integration via SilkTexture.
- Simple GUI with status feedback and logging.

## Requirements
- Python 3.x
- PySide6
- NVIDIA Texture Tools (included in the “files” folder)
- SilkTexture.exe (included in the “files” folder)

## Usage
1. Place your .png files into the “png” folder.
2. Run SpedaTexTool.py.  
3. (Optional) Check the “Use BC7 for Color (C) textures” or “Use BC1 for Gloss (G) textures” checkboxes.
4. Click “Convert PNG -> DDS” to generate .dds files in the “dds” folder.
5. Click “Convert DDS -> .texture” to generate .texture files with SilkTexture.

## License
This project is provided as-is. Refer to each included tool for its respective license.
