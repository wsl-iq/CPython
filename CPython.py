#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2025 
# Developer : Mohammed Al-Baqer

__Developer__ = "Mohammed Al-Baqer"
__Copyright__ = "Copyright (c) 2025"

import os
import shutil
import sys
import time
import keyboard
import subprocess
import ctypes
import glob
import shutil
from datetime import datetime
from CIL.AscallArt import(
    START,
    END,
    sign,
    Enter,
    ERROR,
    INFO,
    Information,
    Working,
    NotWorking,
    warning,
    Complete,
    successfully,
    Failed,
    please,
    Question,
    Help,
    other,
    notice,
    note,
    Running,
    Ready,
    DONE,
    Loading,
    OK,
    Okay,
    stop,
    Critical,
    paused,
    Retrying,
    Skip,
    SCAN,
    Chacking,
    Hacking,
    security,
    AI,
    Press,
    Confirm
)

S = "\033[0m"        # Reset
R = "\033[91;1m"     # Red
G = "\033[92;1m"     # Green
B = "\033[94;1m"     # Blue
Y = "\033[93;1m"     # Yellow
C = "\033[96;1m"     # Cyan
M = "\033[95;1m"     # Magenta
W = "\033[97;1m"     # White
D = "\033[90;1m"     # Grey
P = "\033[38;5;198m" # Pink
O = "\033[38;5;202m" # Orange

Reset = "\033[0m"         # Reset
Black = "\033[40m"        # Black
Dark = "\033[40m"         # Dark
Red = "\033[41m"          # Red
Green = "\033[42m"        # Green
Yellow = "\033[43m"       # Yellow
Blue = "\033[44m"         # Blue
Magenta = "\033[45m"      # Magenta
Cyan = "\033[46m"         # Cyan
White = "\033[47m"        # White
Orange = "\033[48;5;202m" # Orange
Pink = "\033[48;5;198m"   # Pink

def DateTime():
    try:
        now = datetime.now()
        FormatedTime = now.strftime("%I:%M:%S %p")
        FormatedDay = now.strftime("%A")
        DateDay = (
            B + "[" + G + "Today" + B + "]" +
            W + "(" + Y + FormatedDay +
            M + f" {now:%B %d %Y}" +
            W + ") " + B + "[" +
            G + "Time" + B + "]" +
            Y + "[" + R + FormatedTime +
            Y + "]" + W
        )
        return DateDay
    except Exception as e:
        return str(e)

class Main:
    def __init__(self):
        self.StartTime = time.time()
        self.login = "login.txt"
        with open(self.login, "a", encoding="utf-8") as log:
            log.write(f"[START] {time.ctime()}\n")
    
    def ASCLLART(prompt: str) -> str:
        return input(f"\033[91;1m┌─[\033[95;1mMohammed Al-Baqer\033[93;1m@\033[94;1mWSL.IQ\033[91;1m]─[\033[92;1m{prompt}\033[91;1m]\n└──╼\033[91;1m>\033[93;1m>\033[92;1m>\033[97;1m ")

    def Administrator():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def elevate():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    def main(self):
        try:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print(C + "Welcome! The application is starting..." + W)
            print(DateTime())
            AscallArt = R + " ● " + Y + "●" + G + " ● " + W
            print(f"""
┏───────────────────────────────────┓
┃{AscallArt}                            ┃
┣────────────┳──────────────────────┫
┃{B} Developer  {W}│ {__Developer__}{W}    ┃
┃{B} Copyright  {W}│ {__Copyright__}{W}   ┃
┗────────────┻──────────────────────┛""")
            ApplacationStart = time.time()
            
            os.system("python setup.py build_ext --inplace")
            python_version = f"cp{sys.version_info.major}{sys.version_info.minor}"
            pattern = f"mylib.{python_version}-win_amd64.pyd"
            files = glob.glob(pattern)
            if not files:
                raise FileNotFoundError(f"File {pattern} not found")
            pyd_file = files[0]
            print(f"Found PYD: {pyd_file}")

            shutil.copyfile(pyd_file, "mylib.dll")
            dll_path = os.path.abspath("mylib.dll")
            print(f"Created DLL at: {dll_path}")
            os.system(f'python dll.py')
            
            ApplacationDuration = time.time() - ApplacationStart

            print(f"\n{Y}Ran for: {ApplacationDuration:.2f} seconds{W}")
            print(G + "\nPress " + P + "[" + B + "q" + P + "]" + G + " to " + Y + "exit" + G + " or " + Y + "stop" + G + " or " + Y + "Quit" + G + " the session..." + W)
            print(G + "Press " + R + "[" + Y + "Ctrl" + W + " + " + Y + "C" + R + "]" + G + " to " + Y + "exit" + G + " or " + Y + "stop" + G + " the session..." + W)
            print(D + "Or just close the window manually." + W)

            while True:
                if keyboard.is_pressed('q') or keyboard.is_pressed('Ctrl') and keyboard.is_pressed('C'):
                    break
                time.sleep(0.1)

        except KeyboardInterrupt:
            print(G + "Exiting..." + W)

        finally:
            TotalDuration = time.time() - self.StartTime
            with open(self.login, "a", encoding="utf-8") as log:
                log.write(f"[END] {time.ctime()} - Total Duration: {TotalDuration:.2f} seconds\n\n")
            print(f"{G}Total session Duration: {TotalDuration:.2f} seconds.{W}")
            sys.exit(0)

if __name__ == "__main__":
    Main().main()
