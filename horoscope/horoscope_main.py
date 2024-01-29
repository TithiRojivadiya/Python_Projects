import requests
from tkinter import *
from tkinter import ttk
import PIL
import playsound

window = Tk()
window.title("Horoscope app by Tithi")
window.geometry("500x700")

window.mainloop()

# API
# "sunsign_list": "http://sandipbgt.com/theastrologer/api/sunsigns",
# "today": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/today",
