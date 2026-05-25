import subprocess
from time import sleep
from tkinter import filedialog

import customtkinter as ctk
import pyautogui

from interface import achar_arquivo, main

pyautogui.PAUSE = 0.3
arquivo = main()
if arquivo:
    arquivo = arquivo.replace("/", "\\")
    print(arquivo)
    subprocess.run(["powershell", "-command", f"Set-Clipboard -Path '{arquivo}'"])
    subprocess.Popen(
        [r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://claude.ai"],
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    sleep(3.7)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.write(
        "Mande uma versao corrigida (esteticamente, se necessario; gramaticalmente, se tiver erros e repeticoes ou se haver algo que tem como melhorar; e se for uma prova ou algo do tipo, melhore o jeito em que as questões sao feitas, como: se tiverem 7 questões pra 1 ponto, melhore, pois nao há um jeito certo de dividir corretamente) a questao"
    )
    sleep(3.5)
    print("Esperei")
    pyautogui.press("enter")
