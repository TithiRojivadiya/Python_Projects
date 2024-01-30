from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import textwrap
def data_get():
    day = day_name.get()
    sign = sign_name.get()
    link = requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{sign}/{day}").json()

    # Use textwrap.wrap to wrap the text
    wrapped_text = textwrap.wrap(link.get('horoscope'), width=40)

    # Join the wrapped lines into a single string
    reply_text = "\n".join(wrapped_text)

    reply_label.config(text=reply_text)



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

#reply
reply_label = Label(window,text="",font=("Time New Roman",14,"bold"))
reply_label.place(x=25,y=250,height=450,width=440)


#button
button = Button(window,text="GO",font=("Time New Roman",20,"bold"),command=data_get,bg="yellow")
button.place(x=355,y=95,height=110,width=110)


window.mainloop()


