from tkinter import *

class Window(Frame):
    
    def __init__ (self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.chosenColor = StringVar()
        self.chosenColor.set(None)

        optRed = Radiobutton(self,
                             text="Red",
                             variable=self.chosenColor,
                             value="red",
                             command=self.changeColor)
        optRed.grid(row = 0, column = 1)

        optYellow = Radiobutton(self,
                                text="Yellow",
                                variable=self.chosenColor,
                                value="yellow",
                                command=self.changeColor)
        optYellow.grid(row = 0, column = 2)

        optGreen = Radiobutton(self,
                               text="Green",
                               variable=self.chosenColor,
                               value="green",
                               command=self.changeColor)
        optGreen.grid(row = 0, column = 3)


        self.chkBold_Value = StringVar()
        chkBold = Checkbutton(self,
                              text="BOLD",
                              font="time 12 bold",
                              variable=self.chkBold_Value,
                              onvalue="bold",
                              offvalue="",
                              command=self.changeStyle)
        chkBold.grid(row = 1, column = 1)

        self.chkItalic_Value = StringVar()
        chkItalic = Checkbutton(self,
                                text="ITALIC",
                                font="time 12 italic",
                                variable=self.chkItalic_Value,
                                onvalue="italic",
                                offvalue="",
                                command=self.changeStyle)
        chkItalic.grid(row = 1, column = 2)

        self.chkLine_Value = StringVar()
        chkLine = Checkbutton(self,
                              text="UNDERLINE",
                              font="time 12 underline",
                              variable=self.chkLine_Value,
                              onvalue="underline",
                              offvalue="",
                              command=self.changeStyle)
        chkLine.grid(row = 1, column = 3)

        Label(self, text = "Size").grid(row = 0, column = 4, sticky = "sw")
        self.spinSize = Spinbox(self,
                                from_=10,
                                to=20,
                                width=5,
                                command=self.changeStyle)
        self.spinSize.grid(row=1,column=4,sticky="nw",pady=5,padx=5)

        lstStyle_Frame = Frame(self)
        lstStyle_Frame.grid(row = 0, rowspan = 4, column = 0)
        self.lstStyle = Listbox(lstStyle_Frame,
                                font="Times 15",
                                width=10,
                                height=5,
                                selectmode=SINGLE)
        self.lstStyle.bind('<<ListboxSelect>>', self.changeStyle)
        self.lstStyle.selection_set(0)
        self.lstStyle.pack(side = LEFT)
        lstStyle_Scroll = Scrollbar(lstStyle_Frame, orient = VERTICAL)
        lstStyle_Scroll.config(command = self.lstStyle.yview)
        lstStyle_Scroll.pack(side = RIGHT, fill = Y)

        style = ['Helvetica', 'Courier', 'Times', 'Verdana', 'Symbol', 'System']
        i = 0
        for x in style:
            self.lstStyle.insert(i, x)
            i+=1

        self.msgResult = Message(self, text = "One Malayan, Proud Malayan", width = 250, font = "times 10")

        self.msgResult.grid(row = 2, column = 1, columnspan = 3)

        self.pack()

    def changeColor(self):
        self.msgResult.config(fg = str(self.chosenColor.get()))

    def changeStyle(self, *args):
        fontSize = self.spinSize.get()
        font = self.lstStyle.get(self.lstStyle.curselection()[0])
        st = "{0} {1} {2} {3} {4}".format(str(font), str(fontSize), str(self.chkBold_Value.get()), str(self.chkItalic_Value.get()), str(self.chkLine_Value.get()))
        self.msgResult.config(font = st)

root = Tk()
root.title('FontDB_BermudezPaulRonald')
root.geometry("450x130")
app = Window(root)
root.mainloop()
