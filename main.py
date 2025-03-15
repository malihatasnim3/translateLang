import asyncio
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
from langdetect import detect  # Import detect function

# Adding languages to the project
language = googletrans.LANGUAGES
lang_value = list(language.values())
lang1 = list(language.keys())  # Convert dict_keys to list

# Creating a window
window = Tk()
window.title("mimimimi translation")
window.minsize(600, 500)
window.maxsize(600, 500)

translator = Translator()  # Initialize Translator

# Async translation function
async def async_translate(txt, src_lang, dest_lang):
    translated = await translator.translate(txt, src=src_lang, dest=dest_lang)
    return translated.text

# Translate function
def translate():
    global language
    try:
        txt = text1.get(1.0, END).strip()  # Get input text and remove spaces
        c1 = combo1.get()  # Source language
        c2 = combo2.get()  # Target language

        if not txt:
            messagebox.showwarning("Warning", "Please enter text to translate!")
            return

        lan = detect(txt)  # Detect language

        # Get language code for target language
        lan_ = None
        for code, name in language.items():
            if name == c2:
                lan_ = code
                break

        if lan_ is None:
            messagebox.showerror("Error", "Selected target language is invalid!")
            return

        # Run async function to get translated text
        translated_text = asyncio.run(async_translate(txt, lan, lan_))

        text2.delete(1.0, END)
        text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Adding UI components
combo1 = ttk.Combobox(window, values=lang_value, state='r')
combo1.place(x=100, y=20)
combo1.set("Choose a language")

f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)

text1 = Text(f1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

combo2 = ttk.Combobox(window, values=lang_value, state='r')
combo2.place(x=300, y=20)
combo2.set("Choose a language")

f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)

text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

button = Button(window, text='Translate', font=('normal', 15), bg='yellow', command=translate)
button.place(x=230, y=300)

window.mainloop()
