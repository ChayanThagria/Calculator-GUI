from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("Calculator-chayan")

def click(event):
    text_on_button = event.widget.cget("text")
    if text_on_button == "=":
        if screen.get().isdigit():
            value = int(screen.get())

        else:
            value = eval(screen.get())
            mainoutput.set(value)
            screen.update()

    elif text_on_button == "c":
        mainoutput.set("")
        screen.update()

    else:
        mainoutput.set(screen.get()+text_on_button)
        screen.update()


mainoutput = StringVar()
screen = Entry(textvariable = mainoutput,font = "Times 20 bold")
screen.pack(fill = X)

f1 = Frame(root)
f1.pack()

B1 = Button(f1,text ="1",font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f1,text ="2",font = "Times 25 bold" )
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f1,text ="3",font = "Times 25 bold" )
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f1,text ="+" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

f2 = Frame(root)
f2.pack()


B1 = Button(f2,text ="4" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f2,text ="5" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f2,text ="6" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f2,text ="-" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

f3 = Frame(root)
f3.pack()

B1 = Button(f3,text ="7" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f3,text ="8" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f3,text ="9" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f3,text ="*" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

f4 = Frame(root)
f4.pack()

B1 = Button(f4,text ="=" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f4,text ="0" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f4,text ="c" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

B1 = Button(f4,text ="%" ,font = "Times 25 bold")
B1.pack(side = LEFT)
B1.bind("<Button-1>",click)

root.mainloop()

