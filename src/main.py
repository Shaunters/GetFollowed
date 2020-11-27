import pyautogui
import colorama
import os, sys, keyboard
from time import sleep

ARTE = colorama.Fore.BLUE + \
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

"""Função inicial, que retorna qual botão deverá ser usado"""
def chooseButton():
    print(colorama.Fore.LIGHTBLUE_EX + "Escolha qual rede social usando os números abaixo:")
    print("1. Twitter;\n2. Instagram;\n")
    
    option = str(input(">> "))
    
    if option == "1":
        path = "{}/imgs/twitter.png".format(sys.argv[0].split("main.py")[0])
    elif option == "2":
        path = "{}/imgs/instagram.png".format(sys.argv[0].split("main.py")[0])
    elif option not in ("1", "2"):
        print(colorama.Fore.RED + "\nEscolha inválida;" + colorama.Fore.RESET + "\n")
        return chooseButton()

    return path

"""Função que tenta encontrar e retornar o botão"""
def findButton(currentButton, trust=0.8):
    try:
        return pyautogui.locateOnScreen(currentButton, confidence=trust)
    except pyautogui.ImageNotFoundException:
        return None

"""Loop principal que roda até ser parado usando a tecla ESC"""
def mainloop(currentButton):
    while True:

        # Sair se ESC estiver pressionado;
        if keyboard.is_pressed("esc"):
            break

        sleep(1.5)
        # Localizar o botão;
        location = findButton(currentButton)

        # Se não for encontrado, scrollar pra baixo;
        if location == None:
            pyautogui.scroll(-125)
            pass
        else:
            pyautogui.moveTo(location)
            pyautogui.click()
            pass

# Limpando o console (ele também verifica se o SO é Windows ou Linux);
if os.name == "nt":
    os.system("clear")
else:
    os.system("cls")

print(ARTE)

# Chamando a função de escolher o botão;
currentButton = chooseButton()
print(colorama.Fore.YELLOW + "\n\nAVISO:" + colorama.Fore.RESET + \
      " Segure a tecla ESC para fechar! \n\nIniciando em 5 SEG!")

sleep(5)
print(colorama.Fore.GREEN + "\n\nIniciado!\n" + colorama.Fore.RESET)
mainloop(currentButton)
quit()