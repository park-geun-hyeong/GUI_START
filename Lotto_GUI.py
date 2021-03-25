from tkinter import *
from bs4 import BeautifulSoup
import requests

def alert():
    lotto_num = enter.get()

    url='https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}'.format(lotto_num)

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    txt = soup.find('div', attrs={'class','win_result'}).get_text()
    num_list = txt.split('\n')[7:13]
    bonus = txt.split('\n')[-4]
    print("###LOTTO {}회 차 당첨번호###".format(lotto_num))
    print("당첨번호: {}".format(num_list))
    print('보너스: {}'.format(bonus))
    print()

win=Tk()
win.geometry("1000x500")
win.option_add("*Font", '맑은고딕 15')

btn = Button(win)
btn.config(text='button')
btn.config(width=10,height=5)
btn.config(command=alert)
btn.pack()

enter = Entry(win)
enter.pack()

win.mainloop()

import os
os.getcwd()
