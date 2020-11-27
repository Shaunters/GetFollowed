import pyautogui
import colorama
import os, sys, keyboard
from time import sleep

ART = colorama.Fore.BLUE + \
"""
\n\n
   _____      _   ______    _ _                       _ 
  / ____|    | | |  ____|  | | |                     | |
 | |  __  ___| |_| |__ ___ | | | _____      _____  __| |
 | | |_ |/ _ \ __|  __/ _ \| | |/ _ \ \ /\ / / _ \/ _` |
 | |__| |  __/ |_| | | (_) | | | (_) \ V  V /  __/ (_| |
  \_____|\___|\__|_|  \___/|_|_|\___/ \_/\_/ \___|\__,_|
\n\n
"""

# Selecting the button to click;
def chooseButton():
    print(colorama.Fore.LIGHTBLUE_EX + "Escolha qual rede social usando os números abaixo:")
    print("1. Twitter;\n2. Instagram;\n")
    
    option = str(input(">> "))
    
    if option == "1":
        path = "{}/imgs/twitter.png".format(sys.argv[0].split("main.py")[0])
    elif option == "2":
        path = "{}/imgs/instagram.png".format(sys.argv[0].split("main.py")[0])
    elif option not in ("1", "2"):
        print(colorama.Back.RED + "\nEscolha inválida;\n")
        chooseButton()

    return path

# Script main loop;
def mainloop(currentButton):
    running = True
    while running:

        if keyboard.is_pressed("esc"):
            break

        sleep(1.5)
        location = findButton(currentButton)

        if location == None:
            pyautogui.scroll(5)
            pass
        else:
            pyautogui.moveTo(location)
            pyautogui.click()
            pass

# Find and click button;
def findButton(currentButton, trust=0.8):
    try:
        return pyautogui.locateOnScreen(currentButton, confidence=trust)
    except pyautogui.ImageNotFoundException:
        return None

# Clear console and print ART;
if os.name == "nt":
    os.system("clear")
else:
    os.system("cls")

print(ART)

# Get button;
currentButton = chooseButton()
print(colorama.Fore.YELLOW + "\n\nAVISO:" + colorama.Fore.RESET + \
      " Segure a tecla ESC para fechar! \n\nIniciando em 5 SEG!")
sleep(5)
print(colorama.Fore.GREEN + "\n\nIniciado!\n" + colorama.Fore.RESET)
mainloop(currentButton)
quit()