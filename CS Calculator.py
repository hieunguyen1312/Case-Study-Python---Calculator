#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import thu vien tkinter
from tkinter import *
 
# khoi tao bien toan cuc
expression = ""
 
# khoi tao ham cap nhat bieu thuc
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
 
# khoi tao ham chuc nang tinh toan
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" Error ")
        expression = ""
 
 # chuc nang xoa
def clear():
    global expression
    expression = ""
    equation.set("")

# Khoi tao cua so GUI
if __name__ == "__main__":
    gui = Tk()
# cai dat cua so GUI
    gui.configure(background="light green")
    gui.title("CS Calculator")
    gui.geometry("400x300")
# khai bao bien equation voi gia tri rong
equation = StringVar()
# khai bao bien expression_field
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70, ipady=10, padx=5, pady=10)
 
 # khoi tao cac nut bam (bao gom so, dau cham, toan tu và dau bang)
so_1 = Button(gui, text=' 1 ', fg='black', bg='light blue', command=lambda: press(1), height=2, width=10)
so_1.grid(row=2, column=0)
    
so_2 = Button(gui, text=' 2 ', fg='black', bg='light blue', command=lambda: press(2), height=2, width=10)
so_2.grid(row=2, column=1)
 
so_3 = Button(gui, text=' 3 ', fg='black', bg='light blue', command=lambda: press(3), height=2, width=10)
so_3.grid(row=2, column=2)
 
so_4 = Button(gui, text=' 4 ', fg='black', bg='light blue', command=lambda: press(4), height=2, width=10)
so_4.grid(row=3, column=0)

so_5 = Button(gui, text=' 5 ', fg='black', bg='light blue', command=lambda: press(5), height=2, width=10)
so_5.grid(row=3, column=1)
 
so_6 = Button(gui, text=' 6 ', fg='black', bg='light blue', command=lambda: press(6), height=2, width=10)
so_6.grid(row=3, column=2)
 
so_7 = Button(gui, text=' 7 ', fg='black', bg='light blue', command=lambda: press(7), height=2, width=10)
so_7.grid(row=4, column=0)
 
so_8 = Button(gui, text=' 8 ', fg='black', bg='light blue', command=lambda: press(8), height=2, width=10)
so_8.grid(row=4, column=1)
 
so_9 = Button(gui, text=' 9 ', fg='black', bg='light blue', command=lambda: press(9), height=2, width=10)
so_9.grid(row=4, column=2)
 
so_0 = Button(gui, text=' 0 ', fg='black', bg='light blue', command=lambda: press(0), height=2, width=10)
so_0.grid(row=5, column=0)
 
cong = Button(gui, text=' + ', fg='black', bg='violet', command=lambda: press("+"), height=2, width=10)
cong.grid(row=2, column=3)
 
tru = Button(gui, text=' - ', fg='black', bg='yellow', command=lambda: press("-"), height=2, width=10)
tru.grid(row=3, column=3)
 
nhan = Button(gui, text=' * ', fg='black', bg='orange', command=lambda: press("*"), height=2, width=10)
nhan.grid(row=4, column=3)
 
chia = Button(gui, text=' / ', fg='black', bg='brown', command=lambda: press("/"), height=2, width=10)
chia.grid(row=5, column=3)
 
bang = Button(gui, text=' = ', fg='black', bg='pink', command=equalpress, height=2, width=10)
bang.grid(row=5, column=2)
 
xoa = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=2, width=10)
xoa.grid(row=5, column='1')
 
cham = Button(gui, text='.', fg='black', bg='blue', command=lambda: press('.'), height=2, width=10)
cham.grid(row=6, column=0)
    
# goi vong lap su kien, chay chuong trinh
gui.mainloop()


# In[ ]:




