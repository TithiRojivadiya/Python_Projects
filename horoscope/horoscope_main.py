from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk

window = Tk()
window.title("Horoscope app by Tithi")
window.geometry("500x750")

#background
image = Image.open("C:\\Users\\troji\\OneDrive\\Desktop\\Python_Projects\\horoscope\\bg.webp")

# Convert the image to PhotoImage
background_image = ImageTk.PhotoImage(image)
background_label = Label(window, image=background_image)
background_label.place(x=1, y=1, relwidth=1.0, relheight=1.0)

#horoscope label
horoscope_label = Label(window,text="HOROSCOPE APP",font=("Time New Roman",25,"bold"))
horoscope_label.place(x=100,y=20,height=60,width=300)

#sign
sign_name = StringVar()
sign_label = Label(window,text="Sign",font=("Time New Roman",20,"bold"))
sign_label.place(x=25,y=95,height=50,width=100)

sign_list = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
sign_combo = ttk.Combobox(window,values=sign_list,font=("Time New Roman",25,"bold"),textvariable=sign_name)
sign_combo.place(x=135,y=95,height=50,width=200)


#day
day_name = StringVar()
day_label = Label(window,text="Day",font=("Time New Roman",20,"bold"))
day_label.place(x=25,y=155,height=50,width=100)

day_list = ['yesterday','today','tomorrow']
day_combo = ttk.Combobox(window,values=day_list,font=("Time New Roman",25,"bold"),textvariable=day_name)
day_combo.place(x=135,y=155,height=50,width=200)


#button


window.mainloop()

# API
# "sunsign_list": "http://sandipbgt.com/theastrologer/api/sunsigns",
# "today": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/today",
