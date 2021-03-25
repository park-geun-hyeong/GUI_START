from tkinter import *
from datetime import datetime

def alert():
    print("현재의 시각은: {}".format(datetime.now()))

win=Tk()
win.geometry("300x100")
win.title("Time")
win.option_add("*Font","맑은고딕 10")

btn = Button(win)
btn.config(text='current_time')
btn.config(width=10, height=4)
btn.config(command=alert)
btn.pack()

win.mainloop()