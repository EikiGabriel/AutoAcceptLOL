import pyautogui
import time


def check_screen():
    button_pos = pyautogui.locateOnScreen('button_Aceitar.PNG', confidence=0.7)

    if button_pos != None:
        pyautogui.click(button_pos)
        print("partida aceita")
        return True

    return False


def main():

    print("Estou de olho na fila...", end="\n\n")
    while True:
        if check_screen():
            print('Fila Aceita')
            break

while True:
    main()