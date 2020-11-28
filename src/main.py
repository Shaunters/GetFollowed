# OPEN SOURCE IS LIFE
#
# Made by Thiago Souza, 2020
# Github: https://github.com/Shaunters
#
import pyautogui, colorama
import os, sys, keyboard
from time import sleep

# Defines if DEBUG messages appear or not;
DEBUG = False

# Making "shortcuts" to colorama;
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
LBLUE = colorama.Fore.LIGHTBLUE_EX
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET

# ASCII art;
ART = BLUE + \
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

"""Main class, contains all script methods and variables."""
class Main():
    """Initiating the class."""
    def __init__(self, debug=False) -> None:
        self.DEBUG = debug
        # Path to the .png button image;
        self.buttonPath = ""
        # Confidence float used by the locateOnScreen();
        self.confidence = 0.8
        # Waiting time at each iteration of mainLoop();
        self.waitTime = 0.5
        # Scroll size when the button was not found;
        self.scrollAmount = -150

        # Language Sheets containing the languages texts;
        self.englishLS = {
                              "choiceSocial": "Choose the social media to be used: (USE THE NUMBERS)",
                              "choiceError": "\nInvalid choice!\n",
                              "startingWarning": "WARNING -> ",
                              "startingMessage": "The script will start in 5 seconds, open the social media page!\n(Hold ESC to exit!)\n",
                              "startingInit": "Initialized with success!",
                              "closing": "\nClosing..."
                              }
        self.portuguesLS = {
                              "choiceSocial": "Escolha a rede social à ser usada: (USE OS NÚMEROS)",
                              "choiceError": "\nEscolha inválida!\n",
                              "startingWarning": "AVISO -> ",
                              "startingMessage": "O script irá iniciar em 5 segundos,!\n(Segure ESC para sair!)\n",
                              "startingInit": "Iniciado com sucesso!",
                              "closing":"\nFechando..."
                              }
        # Dictionary that will contain the current Language Sheet;
        self.actualLS = self.englishLS

    """Print function made with DEBUG purpouses."""
    def __print(self, texto) -> None:
        if self.DEBUG:
            print(YELLOW + texto)

    """Method to choose the language and set the correct Language Sheets."""
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

    """Returns the input from the user containing the path to the social media button choosed."""
    def __getPathInput(self) -> str:
        print(LBLUE + self.actualLS["choiceSocial"])
        print("1 - Twitter;\n2 - Instagram;\n")
        
        inp = str(input(">> "))
        
        if inp == "1":
            return "{}/imgs/twitter.png".format(sys.argv[0].split("main.py")[0])
        elif inp == "2":
            return "{}/imgs/instagram.png".format(sys.argv[0].split("main.py")[0])
        else:
            print(RESET + RED + self.actualLS["choiceError"] + RESET)
            return self.__getPathInput()

    """Returns the button coordinates, if not found, returns None."""
    def __locateButton(self) -> str or None:
        try:
            temp = pyautogui.locateOnScreen(self.buttonPath, confidence=self.confidence)
            return temp
        except pyautogui.ImageNotFoundException:
            return None
    
    """Main method of the class, called from outside."""
    def run(self) -> None:
        
        os.system("cls" if os.name == "nt" else "clear")
        self.__chooseLanguage()
        print(ART)
        self.buttonPath = self.__getPathInput()

        print("\n\n" + YELLOW + self.actualLS["startingWarning"] + RESET + self.actualLS["startingMessage"])
        sleep(5)
        print("\n" + GREEN + self.actualLS["startingInit"] + RESET)
        if self.DEBUG: print(YELLOW + "(DEBUG MODE)" + RESET)

        self.__mainLoop()
        print(RESET)
        quit()

    """Main loop of the class."""
    def __mainLoop(self) -> None:
        while True:
            self.__print("Running the loop;\n")
            self.__print("Waiting 0.2 seconds;\n")
            sleep(self.waitTime)

            self.__print("Verifying if ESC is pressed;\n")
            if keyboard.is_pressed("ESC"):
                self.__print("ESC is pressed, closing;\n")
                print(RED + self.actualLS["closing"])
                break

            self.__print("Trying to find the button;\n")
            coords = self.__locateButton()
            if coords is None:
                self.__print("Button not found, scrolling down;\n")
                pyautogui.scroll(self.scrollAmount)
                pass
            else:
                self.__print("Button found, moving to it;\n")
                pyautogui.moveTo(coords)
                self.__print("The mouse was moved, clicking;\n")
                pyautogui.click()
                self.__print("Click!\n")
                pass

if __name__ == "__main__":
    try:
        mainC = Main(debug=DEBUG)
        mainC.run()
    except KeyboardInterrupt:
        print(RED + mainC.actualLS["closing"] + RESET)
    except Exception as e:
        print(RED + f"ERROR: \n{e}\n\n" + RESET)
        quit()