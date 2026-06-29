@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 21636)
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 10956)

del /F cleanup-ansys-LAPTOP-GNJ2F7RC-10956.bat
