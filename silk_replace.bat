@echo off
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
