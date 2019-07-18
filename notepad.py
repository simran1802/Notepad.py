from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled Notepad")
    file = None
    text.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documenr","*.txt")])
    if file == "" :
        file = None
    else:
        root.title(os.path.basename(file) + "Notepad")
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documenr","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "Notepad")

    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def Exitmenu():
    root.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Simran")
if __name__ == '__main__':

    root = Tk()
    root.title("Notepad")
    # root.wm_iconbitmap("Cave.ico")
    root.geometry("644x788")

    # Text Area
    text = Text(root,font="lucida 14")
    file = None
    text.pack(expand=TRUE,fill=BOTH)

    # Menubar
    Menubar = Menu(root)
    Filemenu = Menu(Menubar,tearoff=0)
    # Filemenu begins
    # New
    Filemenu.add_command(label="New",command=newFile)

    # Open
    Filemenu.add_command(label="Open",command=openfile)

    # Save
    Filemenu.add_command(label="Save",command=savefile)

    # To add New,open,save seperately
    Filemenu.add_separator()

    # Exit
    Filemenu.add_command(label="Exit",command=Exitmenu)

    # To add New,open,save,exit under 1 menubar
    Menubar.add_cascade(label="File",menu=Filemenu)

    root.config(menu=Menubar)
    # Filemenu ends

    # Editmenu begins
    Editmenu = Menu(Menubar,tearoff=0)

    # To add cut,copy,paste
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit",menu=Editmenu)
    # Editmenu Ends


    # Helpmenu begins
    Helpmenu = Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=Helpmenu)

    # Adding Scroobar
    scrollbar = Scrollbar(text)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)



    root.mainloop()