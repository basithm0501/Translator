# Mini Project created by Basith Mohammed
# Uses tkinter for GUI, tkinter bootstrap for styling, and deep_translator for translating
# August 18th | Basith Mohammed

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttk
from deep_translator import GoogleTranslator, exceptions

# Functions

def translate_now():
    input_text = text1.get("1.0", "end-1c")
    try:
        output_text = GoogleTranslator(source=str(input_language.get()).lower(), target=str(output_language.get()).lower()).translate(text=input_text)
    except exceptions.LanguageNotSupportedException:
        messagebox.showinfo("showinfo", "Please select a language.") 
        print("Select a Language.")
    text2.delete("1.0", "end-1c")
    text2.insert("1.0", output_text)

# Set Up
window = ttk.Window(themename = 'superhero')
window.title("Translator App")
window.geometry("1050x340")

language_list = GoogleTranslator().get_supported_languages()
language_list = [item.upper() for item in language_list]

# Left Side (LS): User Input Side

# LS Variables

input_language = tk.StringVar(value="ENGLISH")
input_text = tk.StringVar()

# LS Widgets 

combo1 = ttk.Combobox(window, values=language_list, state ="r", textvariable = input_language, font = "Calibri 16 bold")
combo1.place(x=100, y=20)
combo1.set("ENGLISH")

f = tk.Frame(window)
f.place(x=10, y=80, width = 440, height = 210)

text1 = tk.Text(f, wrap="word", font = "Calibri 16")
text1.place(x=0,y=0,width=440,height=210)

scrollbar1 = ttk.Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Right Side (RS): Output Side

# RS Variables

output_language = tk.StringVar()
output_text = tk.StringVar()

# RS Widgets

combo2 = ttk.Combobox(window, values=language_list, state ="r", textvariable = output_language, font = "Calibri 16 bold")
combo2.place(x=690, y=20)
combo2.set("SELECT LANGUAGE")

f1 = tk.Frame(window)
f1.place(x=590, y=80, width = 440, height = 210)

text2 = tk.Text(f1, wrap="word", font = "Calibri 16")
text2.place(x=0,y=0,width=440,height=210)

scrollbar2 = ttk.Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button

translate = ttk.Button(window, text = "Translate", bootstyle = "primary", command = translate_now)
translate.place(x = 480, y = 250)

# Run

window.mainloop()