# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:51:36 2023

@author: admin
"""
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

window = tk.Tk()
window.title("Text Editor Application")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def clear():
    txt_edit.delete("1.0","end")


c=Canvas(window,width=1500,height=1500,bg='pink')
c.place(x=0,y=0)
l=Label(window,text="Text Editor Application",font=('Times',24,'bold') ,bg='pink')
l.place(x=500,y=40)
txt_edit = tk.Text()
txt_edit.place(x=340,y=100)
btn_open = tk.Button(window, text="Open...",font=('Times',14,'bold'), command=open_file)
btn_open.place(x=410,y=500)
btn_save = tk.Button(window, text="Save As..",font=('Times',14,'bold'), command=save_file)
btn_save.place(x=580,y=500)
btn_saveas = tk.Button(window, text="Save...",font=('Times',14,'bold'), command=save_file)
btn_saveas.place(x=730,y=500)
btn_cancel = tk.Button(window, text="Cancel...",font=('Times',14,'bold'), command=clear)
btn_cancel.place(x=860,y=500)


window.mainloop()
