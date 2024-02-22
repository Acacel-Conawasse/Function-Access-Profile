from tkinter import Tk, Label, Button, LabelFrame
from threading import Thread
from pynput.keyboard import Listener, Key

class GlobalTabCounter:
    def __init__(self, master):
        self.master = master
        self.tab_count = 0
        self.count_history = []
        self.setup_gui()
        
        # Start listening to keyboard events in a separate thread
        listener_thread = Thread(target=self.start_listening, daemon=True)
        listener_thread.start()

    def setup_gui(self):
        self.master.title("Global Tab Counter")
        
        self.label = Label(self.master, text="Current Tab Count: 0")
        self.label.pack(pady=10)
        
        self.reset_button = Button(self.master, text="Reset and Save Count", command=self.reset_and_save_count)
        self.reset_button.pack(pady=5)
        
        self.history_frame = LabelFrame(self.master, text="Count History")
        self.history_frame.pack(fill='both', expand='yes', padx=10, pady=5)
        
    def start_listening(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    def on_press(self, key):
        if key == Key.tab:
            self.tab_count += 1
            self.update_label()

    def update_label(self):
        # Update GUI elements from the main thread
        self.label.config(text=f"Current Tab Count: {self.tab_count}")
        
    def reset_and_save_count(self):
        if self.tab_count > 0:
            self.count_history.append(self.tab_count)
            self.tab_count = 0
            self.update_label()
            self.update_history()

    def update_history(self):
        # Clear current history
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        # Update history display
        for idx, count in enumerate(self.count_history, start=1):
            Label(self.history_frame, text=f"Count {idx}: {count}").pack(anchor="w")

if __name__ == "__main__":
    root = Tk()
    app = GlobalTabCounter(root)
    root.mainloop()
