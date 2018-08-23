REM Mini Vim for command line, found on this Stack Exchange discussion: https://stackoverflow.com/questions/19497399/basic-text-editor-in-command-prompt
REM This is edited for use with the program (not entering the name every time I edit the file), just for reference.
@echo off
title WinVim
REM color a
cls
echo WinVim 1.02 PostEditor Edition
echo.
echo To save press enter, CTRL+Z, then press enter
echo.
REM echo Make sure to include extension in file name
REM set /p name="File Name":
set name="tempFile"
copy con %name%
REM if exist %name% copy %name% + con
