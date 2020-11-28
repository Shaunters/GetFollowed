# OPEN SOURCE IS LIFE
#
# Made by Thiago Souza, 2020
# Github: https://github.com/Shaunters
#
import pyautogui, colorama
import os, sys, keyboard
from time import sleep

# Define se deve logar prints de DEBUGGING;
DEBUG = False

# Definindo "shortcuts" para o colorama;
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
LBLUE = colorama.Fore.LIGHTBLUE_EX
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET

# Arte ASCII;
ARTE = BLUE + \
"""
\n\n
   _____      _   ______    _ _                       _ 
  / ____|    | | |  ____|  | | |                     | |
 | |  __  ___| |_| |__ ___ | | | _____      _____  __| |
 | | |_ |/ _ \ __|  __/ _ \| | |/ _ \ \ /\ / / _ \/ _` |
 | |__| |  __/ |_| | | (_) | | | (_) \ V  V /  __/ (_| |
  \_____|\___|\__|_|  \___/|_|_|\___/ \_/\_/ \___|\__,_|
\n
"""

"""Classe principal, contém todos os métodos do script"""
class Main():
    """Iniciando a classe, define algumas variáveis."""
    def __init__(self, debug=False) -> None:
        self.DEBUG = debug
        # Caminho para o .png a ser usado;
        self.caminhoBotao = ""
        # Float de confiança, usado pelo locateOnScreen();
        self.confianca = 0.8
        # Tempo de esperar à cada iteração do mainLoop();
        self.waitTime = 0.5
        # Tamanho do scroll quando o botão não for localizado;
        self.scrollAmount = -150

        # Dicionários contendo os textos de várias linguagens;
        self.englishLS = dict({
                              "choiceSocial": "Choose the social media to be used: (USE THE NUMBERS)",
                              "choiceError": "\nInvalid choice!\n",
                              "startingWarning": "WARNING -> ",
                              "startingMessage": "The script will start in 5 seconds, open the social media page!\n(Hold ESC to exit!)\n",
                              "startingInit": "Initialized with success!",
                              "closing":"Closing..."
                              })
        self.portuguesLS = dict({
                              "choiceSocial": "Escolha a rede social à ser usada: (USE OS NÚMEROS)",
                              "choiceError": "\nEscolha inválida!\n",
                              "startingWarning": "AVISO -> ",
                              "startingMessage": "O script irá iniciar em 5 segundos,!\n(Segure ESC para sair!)\n",
                              "startingInit": "Iniciado com sucesso!",
                              "closing":"Fechando..."
                              })
        # Dicionário que irá conter a linguagem usada atualmente;
        self.actualLS = dict({})

    """Função print própria da classe, usada para DEBUGGING."""
    def __print(self, texto) -> None:
        if self.DEBUG:
            print(YELLOW + texto)

    """Função para escolher a linguagem e setar nos Language Sheets (LS) corretos."""
    def __chooseLanguage(self) -> None:
        print("\nWhat language do you want to use?\n")
        print("1. English;\n2. Português Brasileiro;\n")
        inp = str(input(">> "))

        if inp == "1":
            self.actualLS = self.englishLS
            return
        elif inp == "2":
            self.actualLS = self.portuguesLS
            return
        elif inp not in ("1", "2"):
            print("\nInvalid choice!\n")
            return self.__chooseLanguage()

    """Retorna o input do usuário com a rede social escolhida."""
    def __pegarEscolha(self) -> str:
        print(LBLUE + self.actualLS["choiceSocial"])
        print("1 - Twitter;\n2 - Instagram;\n")
        
        inp = str(input(">> "))
        
        if inp == "1":
            return "{}/imgs/twitter.png".format(sys.argv[0].split("main.py")[0])
        elif inp == "2":
            return "{}/imgs/instagram.png".format(sys.argv[0].split("main.py")[0])
        else:
            print(RESET + RED + self.actualLS["choiceError"] + RESET)
            return self.__pegarEscolha()

    """Retorna as coordenadas do botão ou None se não for achado."""
    def __localizarBotao(self) -> str or None:
        try:
            temp = pyautogui.locateOnScreen(self.caminhoBotao, confidence=self.confianca)
            return temp
        except pyautogui.ImageNotFoundException:
            return None
    
    """Método principal, chamado de fora para iniciar a execução."""
    def run(self) -> None:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            self.__chooseLanguage()
            print(ARTE)
            self.caminhoBotao = self.__pegarEscolha()

            print("\n\n" + YELLOW + self.actualLS["startingWarning"] + RESET + self.actualLS["startingMessage"])
            sleep(5)
            print("\n" + GREEN + self.actualLS["startingInit"] + RESET)
            if self.DEBUG: print(YELLOW + "(DEBUG MODE)" + RESET)

            self.__mainLoop()
            print(RESET)
            quit()

        except Exception as e:
            print(RED + f"ERROR: \n{e}\n\n" + RESET)
            quit()
        except KeyboardInterrupt:
            print(RED + self.actualLS["closing"])
            print(RESET)
            return

    """Loop principal, pega a localização e clica."""
    def __mainLoop(self) -> None:
        while True:
            self.__print("Rodando o loop;\n")
            self.__print("Esperando 0.2segs;\n")
            sleep(self.waitTime)

            self.__print("Verificando se ESC está pressionado;\n")
            if keyboard.is_pressed("ESC"):
                self.__print("ESC está pressionado, fechando;\n")
                break

            self.__print("Tentando localizar o botão;\n")
            coords = self.__localizarBotao()
            if coords is None:
                self.__print("O botão não localizado, scrollando;\n")
                pyautogui.scroll(self.scrollAmount)
                pass
            else:
                self.__print("O botão foi localizado, movendo o mouse;\n")
                pyautogui.moveTo(coords)
                self.__print("O mouse foi movido, clickando;\n")
                pyautogui.click()
                self.__print("Click!\n")
                pass

if __name__ == "__main__":
    try:
        Main(debug=DEBUG).run()
    except KeyboardInterrupt:
        pass
