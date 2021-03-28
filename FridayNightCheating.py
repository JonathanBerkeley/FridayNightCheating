from mouseinfo import getPixel as get_pixel
import mouse
import keyboard
import time

class FridayNightCheating:
    standard_click = 0.03
    standard_gap = 0.02
    iv = None
    watch_position = None
    keep_going = True

    def __init__(self, hotkey, key):
        self.hotkey = hotkey
        self.key = key
        pass


    def handle_clicked(self):
        position = mouse.get_position()
        print("Mouse clicked", position)

        self.watch_position = position

        self.iv = get_pixel(position[0], position[1])
        print(self.iv)

        self.main_activity()


    def begin(self):
        print("Put mouse over the up arrow and press", self.hotkey)
        keyboard.add_hotkey(self.hotkey, self.handle_clicked)


    def main_activity(self):
        pixel_changed_count = 0

        while (self.keep_going):
            current_value = get_pixel(self.watch_position[0], self.watch_position[1])

            #Check for death or main menu colours
            if (current_value == (249, 207, 81) or current_value == (0, 0, 0) or current_value == (146, 113, 253)):
                #Verify it wasn't just a stray pixel
                print("Sleeping due to stop pixel found")
                time.sleep(0.1)
                current_value = get_pixel(self.watch_position[0], self.watch_position[1])
                if (current_value == (249, 207, 81) or current_value == (0, 0, 0) or current_value == (146, 113, 253)):
                    print("Stopping due to stop pixel found twice")
                    break

            elif (current_value != self.iv):
                pixel_changed_count += 1
                if (pixel_changed_count > 7):
                    print("Stopping due to constant pixel change")
                    break

                keyboard.press(self.key)
                time.sleep(self.standard_click)
                keyboard.release(self.key)
                print("[", time.ctime()[11:19], "] - Simulated |", self.key, "| Detected change", current_value)
                time.sleep(self.standard_gap)
            
            else:
                pixel_changed_count = 0

        if (not self.keep_going):
            raise KeyboardInterrupt
        else:
            keyboard.remove_hotkey(self.hotkey)
            self.begin()


    def quit(self):
        print("Exit hotkey pressed")
        self.keep_going = False
        raise KeyboardInterrupt