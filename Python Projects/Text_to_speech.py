import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

def convert_to_speech():
    text = input_text.get("1.0", "end-1c")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def clear_text():
    input_text.delete("1.0", tk.END)

# Create the main window
app = tk.Tk()
app.title("Text-to-Speech App")

# Create a scrolled text widget
input_text = scrolledtext.ScrolledText(app, width=50, height=10, wrap=tk.WORD)
input_text.pack(padx=10, pady=10)

# Create buttons
convert_button = tk.Button(app, text="CLICK HERE TO LISTEN :)", bg="blue", fg="white", font=("bold",20), command=convert_to_speech)
convert_button.pack(pady=16)

clear_button = tk.Button(app, text="Clear Text",bg="purple", fg="white", font=("bold",14), command=clear_text)
clear_button.pack(pady=3)

# Run the application
app.mainloop()
