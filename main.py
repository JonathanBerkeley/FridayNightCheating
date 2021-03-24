from mouseinfo import getPixel
import mouse
import keyboard
import time

class track:
    standard_click = 0.03
    standard_gap = 0.02
    iv = None

    hotkey = "alt+a"
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
    print("Put mouse over the left arrow and press", trk.hotkey)
    keyboard.add_hotkey(trk.hotkey, clicked)

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

        #Check for death or main menu colours
        if (current_value == (249, 207, 81) or current_value == (0, 0, 0) or current_value == (146, 113, 253)):
            #Verify it wasn't just a stray pixel
            print("Sleeping due to stop pixel found")
            time.sleep(0.1)
            current_value = getPixel(trk.watch_position[0], trk.watch_position[1])
            if (current_value == (249, 207, 81) or current_value == (0, 0, 0) or current_value == (146, 113, 253)):
                print("Stopping due to stop pixel found twice")
                break

        elif (current_value != trk.iv):
            keyboard.press(key)
            time.sleep(trk.standard_click)
            keyboard.release(key)
            print("[", time.ctime()[11:19], "] - Simulated |", key, "| Detected change", current_value)
            time.sleep(trk.standard_gap)

    if (not trk.keep_going):
        raise KeyboardInterrupt
    else:
        keyboard.remove_hotkey(trk.hotkey)
        begin()


def quit():
    print("Exit hotkey pressed")
    trk.keep_going = False
    raise KeyboardInterrupt

if __name__ == "__main__":
    main()