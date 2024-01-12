from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("TRANSLATOR")
root.geometry("450x750")
root.config(bg="Blue")

#label of TRANSLATOR
lab_text = Label(root,text="TRANSLATOR",font=("Times New Roman",25,"bold"),bg="White")
lab_text.place(x=65,y=15,height=45,width=320)

frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root,text="SOURCE TEXT",font=("Times New Roman",22,"bold"),bg="yellow")
lab_text.place(x=20,y=75,height=30,width=250)

Sor_txt = Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=20,y=120,height=200,width=410)


root.mainloop()
