from mouseinfo import getPixel
import mouse
import keyboard
import time
import sys

class track:
    standard_click = 0.05
    standard_gap = 0.01
    iv = None

    watch_position = None
    keep_going = True

    def __init__(self):
        pass


trk = track()

def main():
    keyboard.add_hotkey('alt+n', quit)
    begin()
    
    while (trk.keep_going):
        time.sleep(1)

def begin():
    print("Put mouse over the left arrow and press alt+a")
    keyboard.add_hotkey('alt+a', clicked)

def test():
    print(mouse.get_position())

def clicked():
    position = mouse.get_position()
    print("Mouse clicked", position)

    trk.watch_position = position

    initial_value = getPixel(position[0], position[1])
    trk.iv = initial_value
    print(initial_value)

    activity('a')


def activity(key):
    while (trk.keep_going):
        current_value = getPixel(trk.watch_position[0], trk.watch_position[1])
        if (current_value != trk.iv):
            keyboard.press(key)
            time.sleep(trk.standard_click)
            keyboard.release(key)
            print("[", time.ctime()[11:19], "] - Simulated |", key, "| Detected change", current_value)
            time.sleep(trk.standard_gap)
        
    if (not trk.keep_going):
        raise KeyboardInterrupt


def quit():
    print("Exit hotkey pressed")
    trk.keep_going = False
    raise KeyboardInterrupt

if __name__ == "__main__":
    main()