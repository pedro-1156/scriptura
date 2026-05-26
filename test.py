import time

import pyautogui

time.sleep(5)
foto = pyautogui.screenshot()
foto.save("foto.png")
