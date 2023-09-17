import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

lang_data = lt.languages()
lang_names = [lang['name'] for lang in lang_data ]
lang_codes = {lang['name']: lang['code']for lang in lang_data}

app = tk.Tk()

app.geometry('700x400')
app.title("Language Exchange")
app.config(bg = "white")


# Input Details
app_name = tk.Label(app, text = "Language Exchange", font = "arial 15 bold", bg = "white")
app_name.place(x = 230, y = 0)

input_label = tk.Label(app, text = "Enter text", font = "arial 13 bold", bg = "white")
app_name.place(x = 230, y = 0)
input_label.place(x = 85, y = 45)

input_text = tk.Text(app, font = "arial 10", height = 11, width = 30, padx = 5)
input_text.place(x = 15, y = 100)

input_lang = ttk.Combobox(app, width = 19, values = lang_names)
input_lang.place(x = 55, y = 75)
input_lang.set("Choose input language")

app_name = tk.Label(app, text = "Language Exchange", font = "arial 15 bold")
app_name.place(x = 230, y = 0)
#---------------------------------------------------------------------------

# Output Details

output_label = tk.Label(app, text = "Output", font = "arial 13 bold", bg = "white")
output_label.place(x = 490, y = 45)

output_text = tk.Text(app, font = "arial 10", height = 11, width = 30, padx = 5)
output_text.place(x = 400, y = 100)

output_lang = ttk.Combobox(app, width = 19, values = lang_names)
output_lang.place(x = 440 , y = 75)
output_lang.set("Choose output language")

#---------------------------------------------------------------------------
# Button

def Translate():
    try:
        trans_text = lt.translate(input_text.get("1.0", tk.END), lang_codes[input_lang.get()], lang_codes[output_lang.get()])
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END , trans_text)
    except KeyError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END , str(e))


trans_btn = tk.Button(app, text = "Translate", font = "arial 10 bold", padx = 5, command = Translate)
trans_btn.place(x = 305, y = 180)  
#---------------------------------------------------------------------------
# Clear Button

def clear():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

clear_btn = tk.Button(app, text = "Clear", font = "arial 10 bold", padx = 5, width = 8, command = clear)
clear_btn.place(x = 305, y = 230)

app.mainloop()