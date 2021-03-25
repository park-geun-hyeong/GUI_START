from tkinter import *
import os

win=Tk()
win.title("Login Program")
win.geometry("600x500")
win.option_add("*Font","맑은고딕 15")

##image
img_path = 'C:/Users/park1/PycharmProjects/pythonProject1/jbnu_img.png'

label3 = Label(win)
img = PhotoImage(file=img_path, master=win)
img = img.subsample(5)
label3.config(image=img)
label3.pack()

## id label
label1 = Label(win)
label1.config(text='Id')
label1.pack()

##id input
enter1=Entry(win)
enter1.insert(0,"aaa@jbnu.ac.kr")

def clear(event):
    enter1.delete(0, len(enter1.get()))
enter1.bind("<Button-1>",clear)
enter1.pack()

## psw label
label2 = Label(win)
label2.config(text='Password')
label2.pack()

##pwd input
enter2=Entry(win)
enter2.config(show='*')
enter2.pack()

## login button

def alert():
    print(f'id: {enter1.get()}')
    print(f'password: {enter2.get()}')
    label4.config(text='Login Success')

btn = Button(win)
btn.config(width=8, height=3)
btn.config(text='Login')
btn.config(command=alert)
btn.pack()

##message
label4 = Label(win)
label4.pack()

win.mainloop()
