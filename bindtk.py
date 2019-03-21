from tkinter import *
window = Tk()
button = Button(text="Нажмите")
def fun(event):
    print('Нажата клавиша Enter')
window.bind("<Return>", fun)
button.pack()
window.mainloop()