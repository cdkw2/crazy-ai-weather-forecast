import tkinter as tk
from tkinter import ttk
import time
import threading

splash_texts = ["Searching location", "Analyzing the clouds...", "Looking outside your window...", "Gathering last information..."]

def open_loading_window():
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    
    style = ttk.Style()
    style.theme_use("default")
    style.configure("green.Horizontal.TProgressbar", troughcolor="white", background="green")
    
    splash_label = tk.Label(loading_window, text="", font=("MS Sans Serif", 10))
    splash_label.pack(padx=20, pady=10)
    
    progress = ttk.Progressbar(loading_window, style="green.Horizontal.TProgressbar", orient="horizontal", length=300, mode="determinate")
    progress.pack(padx=20, pady=10)
    
    def update_splash_text():
        for text in splash_texts:
            splash_label.config(text=text)
            time.sleep(5)
    
    def finish_loading():
        for i in range(101):
            progress["value"] = i
            loading_window.update_idletasks()
            time.sleep(0.2)
            
        loading_window.destroy()
        open_result_window()
    
    loading_thread = threading.Thread(target=finish_loading)
    loading_thread.start()
    
    splash_thread = threading.Thread(target=update_splash_text)
    splash_thread.start()

def open_result_window():
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    
    result_label = tk.Label(result_window, text="Idk, just look outside", font=("MS Sans Serif", 12))
    result_label.pack(padx=20, pady=20)

def submit_button_clicked():
    input_value = input_entry.get()
    if input_value:
        root.withdraw()
        open_loading_window()

root = tk.Tk()
root.title("AI weather forecast")

input_label = tk.Label(root, text="Enter your location:", font=("MS Sans Serif", 10))
input_label.pack(padx=20, pady=20)

input_entry = tk.Entry(root, font=("MS Sans Serif", 10))
input_entry.pack(padx=20, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_button_clicked, font=("MS Sans Serif", 10))
submit_button.pack(padx=20, pady=20)

root.mainloop()