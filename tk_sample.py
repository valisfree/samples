from tkinter import *

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.geometry("450x300+300+300")
        self.master.minsize(350,250)
        self.master.title("Calculator")

        ### STREAM
        self.f_top = LabelFrame(self.master, text='HELLO BRO!')
        self.l1 = Label(self.f_top, width=150, height=5, text="stream", bg='gray', font="Arial 16")
        self.l1['text'] = 'This is label'

        ### TEXT FIELD
        
        # кусок с текстовым полем
        self.text1=Text(self.f_top,height=2,font='Arial 14',wrap=WORD, bg='gray')
        self.text1.pack(side='bottom')
       

        ### PACK
        self.f_top.pack(fill=X, padx=5, pady=5)
        self.l1.pack(fill=X)
        self.master.mainloop()

class AboutProgram:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.title('child')
        self.slave.geometry('200x150+500+375')
        self.text = Text(self.slave, background = 'white')
        self.text.pack(side = TOP, fill = BOTH, expand = YES)
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()

# Start GUI
root = Tk()
gui = Interface(root)
