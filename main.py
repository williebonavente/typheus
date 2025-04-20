import tkinter as tk
from tkinter import ttk
import time

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TypeTrack - Keystroke Feedback Typing System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f4f4f4")

        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.current_index = 0
        self.start_time = None
        self.errors = 0

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="Welcome to TypeTrack", font=("Helvetica", 20, "bold"), bg="#f4f4f4")
        title.pack(pady=20)

        self.text_display = tk.Label(self.root, text=self.sample_text, font=("Courier New", 16), wraplength=700, bg="#f4f4f4")
        self.text_display.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Courier New", 16), width=70)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.on_key_press)

        self.status_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#f4f4f4", fg="gray")
        self.status_label.pack(pady=10)

        self.stats_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.stats_frame.pack(pady=10)

        self.wpm_label = tk.Label(self.stats_frame, text="WPM: 0", font=("Arial", 14), bg="#f4f4f4")
        self.wpm_label.grid(row=0, column=0, padx=10)

        self.accuracy_label = tk.Label(self.stats_frame, text="Accuracy: 100%", font=("Arial", 14), bg="#f4f4f4")
        self.accuracy_label.grid(row=0, column=1, padx=10)

    def on_key_press(self, event):
        if self.start_time is None:
            self.start_time = time.time()

        expected_char = self.sample_text[self.current_index]
        typed_char = event.char

        if typed_char == expected_char:
            self.current_index += 1
            if self.current_index == len(self.sample_text):
                self.end_test()
        else:
            self.errors += 1

        self.update_stats()

    def update_stats(self):
        elapsed_time = time.time() - self.start_time
        elapsed_minutes = elapsed_time / 60

        typed_text = self.entry.get()
        words = len(typed_text.split())
        wpm = int(words / elapsed_minutes) if elapsed_minutes > 0 else 0

        total_typed = len(typed_text)
        correct = total_typed - self.errors if total_typed >= self.errors else 0
        accuracy = (correct / total_typed) * 100 if total_typed > 0 else 100

        self.wpm_label.config(text=f"WPM: {wpm}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")

    def end_test(self):
        self.entry.config(state="disabled")
        self.status_label.config(text="Test complete. Great job!", fg="green")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
