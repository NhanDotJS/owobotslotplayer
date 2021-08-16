import pyautogui
import sys
import time
import random

while True:
    randomvar = random.randint(14, 25)
    if randomvar in range(16, 20):
        pyautogui.click(x=497, y=853)
        pyautogui.write('owo s ' + str(random.randint(1, 20)))
        pyautogui.press('enter')
        time.sleep(random.randint(1, 5))
        pyautogui.write('owo h')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 4))
        pyautogui.write('owo b')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 5))
        pyautogui.write(
            'owo ' + random.choice(
                ["blush", "cry", "dance", "lewd", "pout", "shrug", "sleepy", "smile", "smug", "thumbsup", "wag",
                 "thinking", "triggered", "teehee", "deredere", "thonking", "scoff", "happy", "thumbs", "grin"]))
        pyautogui.press('enter')
        pyautogui.click(x=33, y=696)
        time.sleep(0.5)
        time.sleep(randomvar)
    elif randomvar == 14 or randomvar == 24:
        pyautogui.click(x=497, y=853)
        pyautogui.write('owo zoo')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 8))
        pyautogui.write('owo cf ' + str(random.randint(1, 20)))
        pyautogui.press('enter')
        time.sleep(random.randint(1, 6))
        pyautogui.write('owo cash')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 5))
        pyautogui.write(random.choice(["Abc", "Is IO Gay?",
                        "Nhưng mà ai hỏi?", "hehe", "biết t là bot thế đéo nào đc", "Yêu Linh <3"]))
        pyautogui.press('enter')
        time.sleep(randomvar / (random.randint(2, 3)))
        pyautogui.click(x=36, y=643)
        time.sleep(0.5)
    else:
        pyautogui.click(x=497, y=853)
        pyautogui.write('owo h')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 5))
        pyautogui.write('owo b')
        pyautogui.press('enter')
        time.sleep(random.randint(1, 5))
        pyautogui.write('owo 8b ' + random.choice(["Abc", "Is IO Gay?",
                        "Nhưng mà ai hỏi?", "hehe", "biết t là bot thế đéo nào đc"]))
        pyautogui.press('enter')
        time.sleep(randomvar)
