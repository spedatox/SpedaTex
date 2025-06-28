#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SpedaTex (nvtt_export + SilkTexture Integration) - UI Improved
Created by: Spedatox
Version: 0.8.0 (Enhanced Texture Support with Improved UI)
"""

import os
import sys
import subprocess
from PySide6 import QtWidgets, QtCore, QtGui

appversion = "0.8.0"

class SpedaTexToolWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpedaTex by Spedatox")
        self.setMinimumSize(900, 650)

        # Central widget container
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QtWidgets.QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Initialize paths & UI components
        self.setup_paths()
        self.init_ui_components()
        self.setup_ui()
        self.load_styles()
        self.initialize_log_messages()

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(self.icon_path))

        # Create menu bar
        self.create_menu_bar()

        # Drive connections
        self.connect_signals()

    def create_menu_bar(self):
        """Create a menu bar with basic actions."""
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        exit_action = QtGui.QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Tools menu
        tools_menu = menu_bar.addMenu("Tools")

        convert_action = QtGui.QAction("Start Conversion", self)
        convert_action.triggered.connect(self.start_conversion)
        tools_menu.addAction(convert_action)

        silk_action = QtGui.QAction("Start .texture Conversion", self)
        silk_action.triggered.connect(self.run_silktexture_batch)
        tools_menu.addAction(silk_action)

        clear_log_action = QtGui.QAction("Clear Log", self)
        clear_log_action.triggered.connect(self.log.clear)
        tools_menu.addAction(clear_log_action)

        # Help menu
        help_menu = menu_bar.addMenu("Help")

        credits_action = QtGui.QAction("Credits", self)
        credits_action.triggered.connect(self.show_credits)
        help_menu.addAction(credits_action)

    def init_ui_components(self):
        """Initialize UI components."""
        # Header image
        self.header_image = QtWidgets.QLabel()

        # Log area
        self.log = QtWidgets.QTextEdit()
        self.log.setReadOnly(True)

        # Checkboxes
        self.bc7_color_check = QtWidgets.QCheckBox("Use BC7 for Color (C) textures")
        self.bc7_gloss_check = QtWidgets.QCheckBox("Use BC1 for Gloss (G) textures")
        self.overwrite_checkbox = QtWidgets.QCheckBox("Overwrite existing DDS files")
        self.overwrite_checkbox.setChecked(True)

        # Buttons
        self.convert_button = QtWidgets.QPushButton("Convert PNG -> DDS")
        self.clear_button = QtWidgets.QPushButton("Clear Log")
        self.silk_button = QtWidgets.QPushButton("Convert DDS -> .texture")
        self.credits_button = QtWidgets.QPushButton("Credits")

        # Status bar
        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

    def setup_ui(self):
        """Configure main content layout."""
        # Set up header area
        self.setup_header()

        # Content layout
        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(10)
        self.main_layout.addLayout(content_layout, stretch=1)

        # Utility area: checkboxes, buttons
        utility_group = QtWidgets.QGroupBox("Converter Options")
        utility_layout = QtWidgets.QGridLayout(utility_group)

        utility_layout.addWidget(self.bc7_color_check, 0, 0, 1, 2)
        utility_layout.addWidget(self.bc7_gloss_check, 0, 2, 1, 2)
        utility_layout.addWidget(self.overwrite_checkbox, 1, 0, 1, 4)
        utility_layout.addWidget(self.convert_button, 2, 0, 1, 2)
        utility_layout.addWidget(self.silk_button, 2, 2, 1, 2)
        utility_layout.addWidget(self.clear_button, 3, 0, 1, 2)
        utility_layout.addWidget(self.credits_button, 3, 2, 1, 2)

        content_layout.addWidget(utility_group)

        # Log group
        log_group = QtWidgets.QGroupBox("Conversion Log")
        log_layout = QtWidgets.QVBoxLayout(log_group)
        log_layout.addWidget(self.log)
        content_layout.addWidget(log_group, stretch=1)

    def setup_header(self):
        """Configure a header banner image."""
        header_pixmap = QtGui.QPixmap(self.header_image_path)
        self.header_image.setPixmap(
            header_pixmap.scaledToWidth(self.width(), QtCore.Qt.SmoothTransformation)
        )
        self.header_image.setAlignment(QtCore.Qt.AlignCenter)
        self.header_image.setStyleSheet("""
            QLabel {
                background-color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding: 10px 0;
            }
        """)
        self.main_layout.addWidget(self.header_image)

    def connect_signals(self):
        """Connect UI signals to logic."""
        self.convert_button.clicked.connect(self.start_conversion)
        self.clear_button.clicked.connect(self.log.clear)
        self.silk_button.clicked.connect(self.run_silktexture_batch)
        self.credits_button.clicked.connect(self.show_credits)

    def load_styles(self):
        """Load application stylesheet."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6da8;
            }
            QPushButton#silk_button {
                background-color: #27ae60;
            }
            QPushButton#silk_button:hover {
                background-color: #219a52;
            }
            QPushButton#credits_button {
                background-color: #9b59b6;
            }
            QPushButton#credits_button:hover {
                background-color: #8e44ad;
            }
            QGroupBox {
                margin-top: 10px;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 10px;
            }
            QLabel {
                font-size: 16px;
                color: #ffffff;
            }
            QCheckBox {
                color: #2c3e50;
                font-weight: 500;
            }
            QTextEdit {
                background-color: #f5f6fa;
                color: #2c3e50;
                border: 2px solid #dcdde1;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Consolas';
            }
        """)

        # ObjectName-based styling if needed
        self.silk_button.setObjectName("silk_button")
        self.credits_button.setObjectName("credits_button")

    def setup_paths(self):
        """Initialize file system paths."""
        if getattr(sys, 'frozen', False):
            base_dir_exe = os.path.dirname(sys.executable)
            internal_dir = sys._MEIPASS
        else:
            base_dir_exe = os.path.dirname(os.path.abspath(__file__))
            internal_dir = base_dir_exe

        self.base_dir = base_dir_exe
        self.header_image_path = os.path.join(internal_dir, "files", "header_banner.png")
        self.icon_path = os.path.join(internal_dir, "files", "icon.png")
        self.nvtt_export_dir = os.path.join(internal_dir, "files", "NVIDIA Texture Tools")
        self.nvtt_export_path = os.path.join(self.nvtt_export_dir, "nvtt_export.exe")
        self.source_folder = os.path.join(base_dir_exe, "png")
        self.output_folder = os.path.join(base_dir_exe, "dds")
        self.dont_touch_folder = os.path.join(internal_dir, "files", "Dont Touch")

        # Create required directories if missing
        os.makedirs(self.source_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)

    def initialize_log_messages(self):
        """Initialize log page with config details."""
        self.log.append(f"SpedaTex Texture Conversion Suite Version {appversion}")
        self.log.append("Initialized SpedaTex with following configuration:")
        self.log.append(f"Source Folder: {self.source_folder}")
        self.log.append(f"Output Folder: {self.output_folder}")
        self.log.append("Texture format options:")
        self.log.append(f"- Color: {'BC7' if self.bc7_color_check.isChecked() else 'BC1 (default) - BC7 (optional)'}")
        self.log.append(f"- Glossiness: {'BC1' if self.bc7_gloss_check.isChecked() else 'BC7'}")
        self.log.append("- Normal: BC5")
        self.log.append("- Switchmask: BC4")
        self.log.append("- Fuzz: BC7")
        self.log.append("- Emission: BC7")
        self.log.append("- Mask: BC7")
        self.log.append("- _V: BC7")
        self.log.append("-" * 50)

    def show_credits(self):
        """Show credits in a pop-up dialog."""
        credits_text = f"""SpedaTex Tool
Created by: Spedatox
Version: {appversion}

Credits:
- Okangel (SilkTexture)
- NVIDIA (NVTT Exporter)
- Insomniac Games (Reference Assets)
- Special thanks to TangoTeds and REZA
"""
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Credits")
        msg.setText(credits_text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

    def start_conversion(self):
        """Start PNG->DDS conversion process."""
        if not os.path.exists(self.source_folder) or not os.path.exists(self.nvtt_export_path):
            self.log.append("Error: Required folders or tools not found!")
            self.status_bar.showMessage("Conversion failed: Missing PNG folder or nvtt_export.exe")
            return

        png_files = [f for f in os.listdir(self.source_folder) if f.lower().endswith(".png")]
        if not png_files:
            self.log.append("No PNG files found in source folder.")
            self.status_bar.showMessage("No PNG files found.")
            return

        self.log.append(f"Starting conversion of {len(png_files)} files...")
        self.status_bar.showMessage("Converting PNG -> DDS, please wait...")
        QtCore.QCoreApplication.processEvents()

        for png in png_files:
            full_png_path = os.path.join(self.source_folder, png)
            self.convert_png_to_dds(full_png_path, self.overwrite_checkbox.isChecked())

        self.log.append("Conversion process completed!")
        self.log.append("-" * 50)
        self.status_bar.showMessage("DDS Conversion complete!", 5000)

    def convert_png_to_dds(self, source_png, overwrite):
        """Convert individual PNG file to DDS using nvtt_export.exe."""
        filename = os.path.basename(source_png)
        source_name = os.path.splitext(filename)[0]
        parts = source_name.split('_')
        suffix = parts[-1].lower() if len(parts) > 1 else ""

        # Map suffix to desired format
        format_map = {
            "color": (["--format", "bc7" if self.bc7_color_check.isChecked() else "bc1"], "srgb"),
            "c": (["--format", "bc7" if self.bc7_color_check.isChecked() else "bc1"], "srgb"),
            "basecolor": (["--format", "bc7" if self.bc7_color_check.isChecked() else "bc1"], "srgb"),
            "glossiness": (["--format", "bc1" if self.bc7_gloss_check.isChecked() else "bc7"], "srgb"),
            "g": (["--format", "bc1" if self.bc7_gloss_check.isChecked() else "bc7"], "srgb"),
            "normal": (["--format", "bc5"], "linear"),
            "n": (["--format", "bc5"], "linear"),
            "mask": (["--format", "bc7"], "srgb"),
            "switchmask": (["--format", "bc4"], "linear"),
            "fuzz": (["--format", "bc7"], "srgb"),
            "v": (["--format", "bc7"], "srgb"),
            "e": (["--format", "bc7"], "srgb"),
            "m": (["--format", "bc7"], "srgb"),
        }
        formats, transfer = format_map.get(suffix, (["--format", "bc7"], "srgb"))

        output_filename = f"{source_name}.dds"
        output_path = os.path.join(self.output_folder, output_filename)

        if os.path.exists(output_path) and not overwrite:
            self.log.append(f"Skipped existing file: {output_filename}")
            self.log.append("-" * 50)
            return

        cmd = [
            self.nvtt_export_path,
            *formats,
            "--export-transfer-function", transfer,
            "--output", output_path,
            source_png
        ]

        try:
            self.log.append(f"Processing: {filename}")
            proc = subprocess.run(
                cmd,
                check=True,
                cwd=self.nvtt_export_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if proc.stdout:
                self.log.append(proc.stdout.decode(errors='ignore'))
            self.log.append(f"Successfully created: {output_filename}")
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode(errors='ignore') if e.stderr else str(e)
            self.log.append(f"Conversion failed for {filename}: {error_msg}")
        except Exception as exc:
            self.log.append(f"Unexpected error processing {filename}: {str(exc)}")

        self.log.append("-" * 50)
        QtCore.QCoreApplication.processEvents()

    def run_silktexture_batch(self):
        """Generate and run a batch script for SilkTexture-based .texture generation."""
        batch_content = r"""@echo off
set "DDSFOLDER=%~dp0dds"
set "ORIGINALFOLDER=%~dp0_internal\files\Dont Touch"
set "OUTPUTFOLDER=%~dp0texture"
set "SILK_EXE=%~dp0_internal\files\SilkTexture.exe"

:: Optional extra parameters
set "EXTRASD="
set "IGNOREFORMAT=--ignoreformat"
set "TESTMODE="

echo ==========================================
echo  DDS -> .texture automation starting...
echo ==========================================

IF NOT EXIST "%SILK_EXE%" (
  echo [Error] SilkTexture.exe not found: %SILK_EXE%
  pause
  exit /b 1
)

:: 1) Color (C)
IF EXIST "%ORIGINALFOLDER%\texture_C.texture" (
  for %%I in ("%DDSFOLDER%\*_C.dds") do (
    echo [Color] Creating your color texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_C.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_C.texture" not found in "Dont Touch" folder, skipping...
)

:: 2) Gloss (G)
IF EXIST "%ORIGINALFOLDER%\texture_G.texture" (
  for %%I in ("%DDSFOLDER%\*_G.dds") do (
    echo [Gloss] Creating your glossieness texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_G.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_G.texture" not found in "Dont Touch" folder, skipping...
)

:: 3) Normal (N)
IF EXIST "%ORIGINALFOLDER%\texture_N.texture" (
  for %%I in ("%DDSFOLDER%\*_N.dds") do (
    echo [Normal] Creating your normal texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_N.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_N.texture" not found in "Dont Touch" folder, skipping...
)

:: 4) Mask (mask)
IF EXIST "%ORIGINALFOLDER%\texture_mask.texture" (
  for %%I in ("%DDSFOLDER%\*_mask.dds") do (
    echo [Mask] Creating your mask texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_mask.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_mask.texture" not found in "Dont Touch" folder, skipping...
)

:: 5) Switchmask
IF EXIST "%ORIGINALFOLDER%\texture_switchmask.texture" (
  for %%I in ("%DDSFOLDER%\*_switchmask.dds") do (
    echo [Switchmask] Creating your switchmask texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_switchmask.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_switchmask.texture" not found in "Dont Touch" folder, skipping...
)

:: 6) Fuzz
IF EXIST "%ORIGINALFOLDER%\texture_fuzz.texture" (
  for %%I in ("%DDSFOLDER%\*_fuzz.dds") do (
    echo [Fuzz] Creating your fuzz texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_fuzz.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_fuzz.texture" not found in "Dont Touch" folder, skipping...
)

:: 7) V Map
IF EXIST "%ORIGINALFOLDER%\texture_v.texture" (
  for %%I in ("%DDSFOLDER%\*_v.dds") do (
    echo [V Map] Creating your v texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_v.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_v.texture" not found in "Dont Touch" folder, skipping...
)

:: 8) Misc (M)
IF EXIST "%ORIGINALFOLDER%\texture_M.texture" (
  for %%I in ("%DDSFOLDER%\*_m.dds") do (
    echo [Misc] Creating your miscellaneous texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_m.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_M.texture" not found in "Dont Touch" folder, skipping...
)

:: 9) Emission (E)
IF EXIST "%ORIGINALFOLDER%\texture_E.texture" (
  for %%I in ("%DDSFOLDER%\*_E.dds") do (
    echo [Emission] Creating your emission texture from %%~nxI ...
    "%SILK_EXE%" replace ^
      "%ORIGINALFOLDER%\texture_E.texture" ^
      "%%~fI" ^
      -o "%OUTPUTFOLDER%" ^
      %EXTRASD% %IGNOREFORMAT% %TESTMODE%
    echo --------------------------------------------------------
  )
) ELSE (
  echo [Warning] "texture_E.texture" not found in "Dont Touch" folder, skipping...
)

echo ==========================================
echo  SpedaTex finished all operations. Output folder:
echo  %OUTPUTFOLDER%
echo ==========================================
pause
"""

        bat_path = os.path.join(self.base_dir, "silk_replace.bat")
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(batch_content)

        self.log.append("Running SilkTexture batch process...")
        self.log.append(f"Batch path: {bat_path}")

        self.process = QtCore.QProcess(self)
        self.process.setWorkingDirectory(self.base_dir)
        self.process.readyReadStandardOutput.connect(self.read_silk_output)
        self.process.readyReadStandardError.connect(self.read_silk_error)
        self.process.started.connect(lambda: self.log.append("SilkTexture batch started."))
        self.process.finished.connect(
            lambda code, status: self.log.append(f"SilkTexture batch finished with code {code}."))
        self.process.start("cmd", ["/c", bat_path])

        self.status_bar.showMessage("Running SilkTexture batch...", 5000)

    def read_silk_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        if output.strip():
            self.log.append(output.strip())

    def read_silk_error(self):
        error = self.process.readAllStandardError().data().decode()
        if error.strip():
            self.log.append(f"[SILKTEXTURE ERROR] {error.strip()}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SpedaTexToolWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
