# main.py

import tkinter as tk
from datetime import datetime
from pynput import keyboard
import pandas as pd
import os

# Constants
LOG_DIR = "data/sessions"
os.makedirs(LOG_DIR, exist_ok=True)

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TypeSense - Typing Feedback System")
        self.root.geometry("800x400")
        self.session_data = []

        # Build UI
        self.build_interface()

        # Keyboard listener
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def build_interface(self):
        self.label = tk.Label(self.root, text="Start typing below. Your keystrokes are being tracked.",
                              font=("Segoe UI", 14))
        self.label.pack(pady=10)

        self.textbox = tk.Text(self.root, height=10, font=("Consolas", 14))
        self.textbox.pack(padx=20, pady=10, fill="both", expand=True)
        self.textbox.focus_set()

        self.save_btn = tk.Button(self.root, text="Save Session", command=self.save_session)
        self.save_btn.pack(pady=10)

    def on_key_press(self, key):
        try:
            self.session_data.append({
                "timestamp": datetime.now(),
                "key": key.char,
                "event": "press"
            })
        except AttributeError:
            self.session_data.append({
                "timestamp": datetime.now(),
                "key": str(key),
                "event": "press"
            })

    def on_key_release(self, key):
        try:
            self.session_data.append({
                "timestamp": datetime.now(),
                "key": key.char,
                "event": "release"
            })
        except AttributeError:
            self.session_data.append({
                "timestamp": datetime.now(),
                "key": str(key),
                "event": "release"
            })

    def save_session(self):
        df = pd.DataFrame(self.session_data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{LOG_DIR}/typing_session_{timestamp}.csv"
        df.to_csv(filename, index=False)
        self.label.config(text=f"Session saved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
