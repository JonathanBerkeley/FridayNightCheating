from FridayNightCheating import FridayNightCheating
from keyboard import add_hotkey
from time import sleep

fnc = FridayNightCheating("alt+d", 'd')

def main():
    add_hotkey('alt+n', fnc.quit)
    fnc.begin()
    
    while (fnc.keep_going):
        sleep(1)

if __name__ == "__main__":
    main()