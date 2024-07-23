from tkinter import *

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        #Widget Container
        self.init__window()

    def init__window(self):
        #LABEL START-----

        Label(self,text="Font").grid(row=0,column=0,sticky="nswe")
        Label(self,text="Font color").grid(row=0,column=1,sticky="nswe")
        Label(self,text="Size").grid(row=0,column=2,sticky="nswe")
        Label(self,text="Preview").grid(row=4,column=1,sticky="nswe")

        #LABEL END-------
        ##########
        #LIST BOX 1 START-----

        #Create listbox
        frmlist1=Frame(self)
        self.lstStyle1=Listbox(frmlist1,font="times 10",width=10,height=5,exportselection=0)
        self.lstStyle1.pack(side=LEFT)

        #Add items in listbox using insert()
        style=['Times','Calibri','Arial','Tahoma','Century','Verdana','Monotype','Georgia','Garamond','Forte']
        i=0
        for x in style:
            self.lstStyle1.insert(i,x)
            i+=1
        
        #Set first item in the list as default selected
        self.lstStyle1.selection_set(0)

        #Listbox event command
        self.lstStyle1.bind('<<ListboxSelect>>',self.changeStyle)

        #Create scrollbar in listbox
        scrollbar=Scrollbar(frmlist1,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)

        #Connect scrollbar to listbox
        scrollbar.config(command=self.lstStyle1.yview)

        #Organize listbox
        frmlist1.grid(row=1,rowspan=2,column=0)

        #LIST BOX 1 END-------
        ##########
        #LIST BOX 2 START-----

        #Create listbox
        frmlist2=Frame(self)
        self.lstStyle2=Listbox(frmlist2,font="times 10",width=10,height=5,exportselection=0)
        self.lstStyle2.pack(side=LEFT)

        #Add items in listbox using insert()
        color=['red','green','black','white','blue','lavender','pink','yellow','orange','sky blue']
        i=0
        for x in color:
            self.lstStyle2.insert(i,x)
            self.lstStyle2.itemconfig(i,{'bg':x,'fg':x})
            i+=1
        
        #Set first item in the list as default selected
        self.lstStyle2.selection_set(0)

        #Listbox event command
        self.lstStyle2.bind('<<ListboxSelect>>',self.changeStyle)

        #Create scrollbar in listbox
        scrollbar=Scrollbar(frmlist2,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)

        #Connect scrollbar to listbox
        scrollbar.config(command=self.lstStyle2.yview)

        #Organize listbox
        frmlist2.grid(row=1,rowspan=2,column=1)

        #LIST BOX 2 END-------
        ##########
        #SPIN BOX START-----

        #Create spinbox
        self.spnSize = Spinbox(self,from_=10,to=72,width=5,command=self.changeStyle)

        #Organize spinbox
        self.spnSize.grid(row=1,column=2,pady=5,padx=5)
        
        #SPIN BOX END-------
        ##########
        #CHECK BUTTONS START-----

        #Variables for the check buttons
        self.b = StringVar()
        self.i = StringVar()
        self.l = StringVar()

        #Create check buttons
        chkBold = Checkbutton(self,text="BOLD",font="times 10 bold",variable=self.b,onvalue="bold",offvalue="",command=self.changeStyle)
        chkItalic = Checkbutton(self,text="ITALIC",font="times 10 italic",variable=self.i,onvalue="italic",offvalue="",command=self.changeStyle)
        chkLine = Checkbutton(self,text="UNDERLINE",font="times 10 underline",variable=self.l,onvalue="underline",offvalue="",command=self.changeStyle)

        #Organize check buttons
        chkBold.grid(row=3,column=0)
        chkItalic.grid(row=3,column=1)
        chkLine.grid(row=3,column=2)

        #CHECK BUTTONS END-------
        ##########
        #PREVIEW START-----

        self.preview = Message(self)
        self.preview.config(relief='solid',width=100,pady=50,padx=200)
        self.preview.grid(row=5,columnspan=3,column=0)
        self.changeStyle()
        
        #PREVIEW END-------
        
        #Place widgets in window
        self.pack()

    #Radio button command

    #Check button, spinbox, and listbox command
    def changeStyle(self, *args):
        #Get spinbox value
        n=self.spnSize.get()
        #Get listbox value
        self.previewMessage = self.lstStyle1.get(self.lstStyle1.curselection()[0])
        self.preview.config(text=self.previewMessage)
        stylo=self.lstStyle1.get(self.lstStyle1.curselection()[0])
        #Get listbox value
        self.preview.config(fg = self.lstStyle2.get(self.lstStyle2.curselection()[0]))
        #Gets format
        st = "{0} {1} {2} {3} {4}".format(str(stylo),str(n),str(self.b.get()),str(self.i.get()),str(self.l.get()))
        #Applies format to message
        self.preview.config(font=st)
                                 

root = Tk()
root.title('FDB2_BermudezPaulRonald')
root.geometry("500x300")
app = Window(root)
root.mainloop()
