import pyautogui
import time

def check_screen():
    button_pos = pyautogui.locateOnScreen('button_Aceitar.PNG', confidence=0.7)
    
    if button_pos != None:
        pyautogui.click(button_pos)
        print("partida aceita")
        return True
    else:
        return False

while True:
    print("Estou de olho na fila...", end="\n\n")
    if check_screen():
        print('Fila Aceita')
            break
    else:
        time.sleep(0.2)
