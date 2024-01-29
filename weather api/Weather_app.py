from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=337a0cd6a0657508814fd54c2b128c16").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(round(int(data["main"]["temp"])-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("WEATHER APP")
win.geometry("500x500")

# Open the image using Pillow
image = Image.open('C:\\Users\\troji\\OneDrive\\Desktop\\Python_Projects\\weather api\\background.jpg')

# Convert the image to PhotoImage
background_image = ImageTk.PhotoImage(image)
background_label = Label(win, image=background_image)
background_label.place(x=1, y=1, relwidth=1.0, relheight=1.0)

#Lable "Weather app"
name_label = Label(win,text="WEATHER APP",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=20,height=65,width=450)

#making combobox
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text=" ",values=list_name,font=("Time New Roman",22,"bold"),textvariable=city_name)
com.place(x=25,y=100,height=55,width=420)

w_label = Label(win,text="Weather Climate :",font=("Time New Roman",15,"bold"))
w_label.place(x=35,y=240,height=50,width=200)
w_label1 = Label(win,text="",font=("Time New Roman",15,"bold"))
w_label1.place(x=235,y=240,height=50,width=200)

wb_label = Label(win,text="Weather Description:",font=("Time New Roman",12,"bold"))
wb_label.place(x=35,y=290,height=50,width=200)
wb_label1 = Label(win,text="",font=("Time New Roman",15,"bold"))
wb_label1.place(x=235,y=290,height=50,width=200)

temp_label = Label(win,text="Temperature :",font=("Time New Roman",15,"bold"))
temp_label.place(x=35,y=340,height=50,width=200)
temp_label1 = Label(win,text="",font=("Time New Roman",15,"bold"))
temp_label1.place(x=235,y=340,height=50,width=200)

per_label = Label(win,text="Pressure :",font=("Time New Roman",15,"bold"))
per_label.place(x=35,y=390,height=50,width=200)
per_label1 = Label(win,text="",font=("Time New Roman",15,"bold"))
per_label1.place(x=235,y=390,height=50,width=200)

#Button
done_button = Button(win,text="Go",font=("Time New Roman",20,"bold"),relief=RAISED,bg="yellow",command=data_get)
done_button.place(x=190,y=165,height=40,width=100)

win.mainloop()
