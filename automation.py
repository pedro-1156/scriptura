import subprocess
from time import sleep
from tkinter import filedialog
import pyperclip

import customtkinter as ctk
import pyautogui
# caminho

from interface import *

pyautogui.PAUSE = 0.3
lista = main()
arquivo = lista[0]
prompt = lista[1]

print(lista)

if arquivo and prompt:
    arquivo = arquivo.replace("/", "\\")
    subprocess.run(["powershell", "-command", f"Set-Clipboard -Path '{arquivo}'"])
    subprocess.Popen(
        [r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://claude.ai"],
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    sleep(4)
    pyautogui.hotkey("ctrl", "v")
    pyperclip.copy(prompt)
    pyautogui.hotkey("ctrl", "v")
    sleep(1)
    pyautogui.press("enter")
