import tkinter as tk
from pynput import keyboard
import threading
import queue

counter = 0
key_queue = queue.Queue()

def increment():
    global counter
    counter += 1

def update_label():
    label.config(text=str(counter))  # 更新UI部分放在这个函数中
    label.after(100, update_label)  # 每100毫秒更新一次标签

def process_queue():
    while not key_queue.empty():
        key_queue.get()  # 从队列中取出一个键
        increment()  # 更新计数器
    window.after(100, process_queue)  # 定期调用自身检查队列

def on_press(key):
    key_queue.put(key)  # 将按下的键放入队列

def start_listen():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# 创建主窗口
window = tk.Tk()
window.title("Keyboard Counter")
window.geometry("300x300")

label = tk.Label(window, text=str(counter), font=("Arial", 50))
label.pack(pady=40)

# 启动监听线程
listener_thread = threading.Thread(target=start_listen, daemon=True)
listener_thread.start()

# 启动定时检查队列并更新标签
update_label()  # 启动标签更新
process_queue()  # 启动队列处理

# 启动主循环
window.mainloop()
