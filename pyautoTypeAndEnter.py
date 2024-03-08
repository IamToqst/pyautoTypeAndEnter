# author:
# █ ▄▀█ █▀▄▀█ ▀█▀ █▀█ █▀█ █▀ ▀█▀
# █ █▀█ █░▀░█ ░█░ █▄█ ▀▀█ ▄█ ░█░
# name:
# 𝐩𝐲𝐚𝐮𝐭𝐨𝐓𝐲𝐩𝐞𝐀𝐧𝐝𝐄𝐧𝐭𝐞𝐫
# description:
# The "pyautoTypeAndEnter" script is a Python program designed to automate the process of typing a specified text and pressing the 'Enter' key at regular intervals. This script utilizes the pyautogui library to simulate keyboard actions, allowing users to input repetitive text without manual intervention. The time interval between each execution can be customized to meet individual preferences.
# warning: 
# This script can be used for automating repetitive tasks, but it should be employed responsibly and ethically. Automated actions in certain contexts may violate terms of service or policies, so ensure compliance with relevant guidelines.

import time
import pyautogui

def type_and_enter(text):
    while True:
        # If you want to adjust the seconds before it auto types text and enters just change the number you see below.
        time.sleep(5)
        pyautogui.typewrite(text)
        pyautogui.press('enter')
if __name__ == "__main__":
    # Replace "YOUR_TEXT_HERE" with the text you want to type
    text_to_type = "YOUR_TEXT_HERE"
    
    type_and_enter(text_to_type)
