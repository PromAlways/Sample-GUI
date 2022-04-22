
from tkinter import *
from tkinter import ttk
from tkinter import commondialog
import webbrowser # lib : Tk interface
import pyautogui as pg

GUI = Tk()
GUI.title(' ทำได้เพียงปลายนิ้ว ')
GUI.geometry('400x300')

def Calender():
    pg.click(1860,1053) # position mouse

B1 = Button(GUI,text='Calender',command=Calender)
B1.pack(ipadx=20,ipady=20,pady=20)

def Windows():
    pg.click(602,1048)  # position mouse

B2 = ttk.Button(GUI,text='Windows',command=Windows)
B2.pack(ipadx=20,ipady=20,pady=20)

def Google():
    webbrowser.open('https://google.com')
B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()