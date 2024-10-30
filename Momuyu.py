import tkinter as tk

from pynput import keyboard
import threading

counter = 0

def increment():
    global counter
    counter += 1
    label.config(text=str(counter))

window = tk.Tk()
window.title("Keyboard-counter")
window.geometry("300x200")

label = tk.Label(window, text=str(counter), font=("Arial",50))
label.pack(pady=40)

def on_press(key):
    increment()

def start_listen():
    with keyboard.listener(on_press=on_press) as listener:
        listener.join()

listener_thread = threading.Thread(target=start_listen(), daemon=True)
listener_thread.start()

window.mainloop()
