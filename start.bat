@echo off
mode con: cols=80 lines=25
title Bot Development testing
REM replace with your bot folder path
cd /d "C:\Users\name\Desktop\bots\Welcomer"
chcp 65001 >nul
echo.  
echo.  
for /f "delims=" %%i in ('"echo prompt $E|cmd"') do set "ESC=%%i"

echo                                [38;2;153;0;255m██████╗  ██████╗ ████████╗    ██████╗ ███████╗██╗   ██╗[0m
echo                                [38;2;178;51;255m██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝██║   ██║[0m
echo                                [38;2;204;102;255m██████╔╝██║   ██║   ██║       ██║  ██║█████╗  ██║   ██║[0m
echo                                [38;2;229;153;255m██╔══██╗██║   ██║   ██║       ██║  ██║██╔══╝  ╚██╗ ██╔╝[0m
echo                                [38;2;255;178;255m██████╔╝╚██████╔╝   ██║       ██████╔╝███████╗ ╚████╔╝ [0m
echo                                [38;2;255;204;255m╚═════╝  ╚═════╝    ╚═╝       ╚═════╝ ╚══════╝  ╚═══╝ [0m
echo                         [38;2;255;153;255m                Bot Dev portal for Development testing                [0m
echo.
echo [38;2;255;153;255m                                             Starting the Discord bot...
echo.
echo.
REM replace with your bot file
                                                                            python Welcomer.py
echo.
echo.
echo.
echo Bot has stopped. Press any key to close...

pause > nul
[0m