import subprocess

file_path = "/Users/k.abe/PycharmProjects/xmindcmd/example_xmind/sample.xmind"
subprocess.run(["open", "-a", "xmind", file_path])

import pyautogui
import time

pyautogui.hotkey("command", "tab")
time.sleep(1)

# ショートカットをpngのエクスポートに割り当てた場合
pyautogui.hotkey("command", "shift", "f")
time.sleep(1)
