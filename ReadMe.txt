Developed by: Spedatox
SilkTexture by: Okangel

⚠️ Important: The /_internal directory contains essential runtime and configuration files. Do not modify or delete its contents. Tampering with this folder may break core functionality.

# SpedaTex - Advanced Texture Conversion Suite


Texture conversion suite for Marvel's Spider-Man 2 modding, supporting both DDS conversion and .texture packaging.

🧠 Features

✅ Convert .png files to .dds with custom compression settings.

✅ Format-specific options (Color, Gloss, Normal, Emission, etc.)

✅ .texture creation via pre-configured .bat batch script.

✅ Built-in SilkTexture automation.

✅ Clean, responsive GUI with smart log system.

✅ Auto-detects project directory, handles paths internally.


🧪 Supported Texture Types
SpedaTex automatically detects the suffix of the texture filename (e.g. _C, _G, _N, etc.) and applies the appropriate compression format.

Suffix
_C		BC7 or BC1	sRGB
_G		BC1 or BC7	Linear
_N		BC5	Linear
_mask		BC7	sRGB
_switchmask	BC4	Linear
_fuzz		BC7	sRGB
_v		BC7	sRGB
_e		BC1	sRGB
_m		BC7	sRGB


🧪 Detailed Usage Guide
SpedaTex is designed for artists and modders who want a no-nonsense texture conversion tool. Follow these steps to go from .png to .dds and finally .texture with minimal hassle and maximum control.

🔹 1. Prepare Your PNG Files
Place all your source .png textures inside the png/ folder.

File Naming Matters!
SpedaTex uses the suffix of each filename to decide which compression format to use.

Filename Example
helmet_C.png	
helmet_G.png	
helmet_N.png	
helmet_mask.png	
helmet_fuzz.png	
helmet_v.png	
helmet_e.png	
helmet_m.png	

✅ You can use lowercase or uppercase suffixes. SpedaTex can handle both.

🔹 2. Launch the App

 run the .exe file which is a standalone executable.

A sleek 800x600 UI will appear with conversion options, logs, and control buttons.


🔹 3. Configure Options
✅ Format Toggles

BC7 for Color (C): Use high-quality BC7 compression for color maps.

BC1 for Gloss (G): Use lighter BC1 for gloss/roughness maps.

These affect how SpedaTex chooses compression for each texture type.

✅ Overwrite Mode

Enabled by default.

If unchecked, existing .dds files will be skipped during conversion.

🔹 4. Start PNG to DDS Conversion
Click “Start DDS Conversion”

SpedaTex will:

Scan the png/ folder.

Match each file’s suffix to a format preset.

compress and convert to .dds.

Save the output into the dds/ folder.

💬 Real-time logs will show conversion status and any issues.

🔹 5. Generate .texture Files via SilkTexture
Click “Start .texture Conversion”

SpedaTex will:

Dynamically create and execute a silk_replace.bat batch script.

For each DDS file, use SilkTexture.exe to replace textures inside reference .texture files 

Outputs the final .texture files to the /texture directory.


🔹 6. View Output
Converted .dds files → dds/ folder

Final .texture files → texture/ folder

🧹 Bonus Controls
Clear Log – Wipes the log output panel

⚠️ Important: The /_internal directory contains essential runtime and configuration files. Do not modify or delete its contents. Tampering with this folder may break core functionality.

🎯 Quick Workflow Summary

Step 1 → Add your PNGs to /png
Step 2 → Launch SpedaTex
Step 3 → Set compression preferences
Step 4 → Click 'Start DDS Conversion'
Step 5 → Click 'Start .texture Conversion'
Step 6 → Find your outputs in /dds and /texture


All paths are handled automatically, no need to manually configure anything unless you move the tool files.