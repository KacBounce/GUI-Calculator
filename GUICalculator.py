from tkinter import *
from tkinter import ttk

global continuee
continuee = False
#TODO Make it work with more then 2 numbers
def Quit(event):
    root.quit()
def Ultimate(event):
    global symbol
    global num1
    global num2
    global result
    global before
    global continuee
    if symbol == "+":
        if continuee:
            GetSum(result,num2)
        else:
            GetSum(num1,num2)
            continuee = True
    elif symbol == "-":
        if continuee:
            GetSub(result,num2)
        else:
            GetSub(num1,num2)
            continuee = True
    elif symbol == "/":
        if continuee:
            GetDiv(result,num2)
        else:
            GetDiv(num1,num2)
            continuee = True
    elif symbol == "*":
        if continuee:
            GetMul(result,num2)
        else:
            GetMul(num1,num2)
            continuee = True
    num2 = ""
    symbol = ""

def clear():
    Equals.delete(0,"end")

def Clear(event):
    global result
    global num1
    global num2
    global continuee
    global before
    result = 0
    num1 = ""
    num2 = ""
    continuee = False
    before = not before
    clear()

def Numbers1(event):
    if before == True:
        global num1
        global num2
        num1 += "1"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "1"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers2(event):
    global num1
    global num2
    if before == True:
        num1 += "2"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "2"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers3(event):
    global num1
    global num2
    if before == True:
        num1 += "3"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "3"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers4(event):
    global num1
    global num2
    if before == True:
        num1 += "4"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "4"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers5(event):
    global num1
    global num2
    if before == True:
        num1 += "5"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "5"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers6(event):
    global num1
    global num2
    if before == True:
        num1 += "6"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "6"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers7(event):
    global num1
    global num2
    if before == True:
        num1 += "7"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "7"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers8(event):
    global num1
    global num2
    if before == True:
        num1 += "8"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "8"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers9(event):
    global num1
    global num2
    if before == True:
        num1 += "9"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "9"
        Equals.delete(0,"end")
        Equals.insert(0,num2)

def Numbers0(event):
    global num1
    global num2
    if before == True:
        num1 += "0"
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "0"
        Equals.delete(0,"end")
        Equals.insert(0,num2)
def Numbersdot(event):
    global num1
    global num2
    if before == True:
        num1 += "."
        Equals.delete(0,"end")
        Equals.insert(0,num1)
    else:
        num2+= "."
        Equals.delete(0,"end")
        Equals.insert(0,num2)
def symbolC(event):
    global before
    global symbol
    global continuee
    if continuee == False:
        before = not before
    symbol = "C"

def symbolX(event):
    global before
    global symbol
    global continuee
    if continuee == False:
        before = not before
    symbol = "X"

def symbolpl(event):
    global before
    global symbol
    global continuee
    if not continuee:
        before = not before
    symbol = "+"

def symbolmin(event):
    global before
    global symbol
    global continuee
    if continuee == False:
        before = not before
    symbol = "-"

def symboldiv(event):
    global before
    global symbol
    global continuee
    if continuee == False:
        before = not before
    symbol = "/"

def symbolmul(event):
    global before
    global symbol
    global continuee
    if continuee == False:
        before = not before
    symbol = "*"

def GetSum(num1,num2):
    global result
    result = float(num1) + float(num2)
    result = float("{0:.2f}".format(result))
    Equals.delete(0,"end")
    Equals.insert(0,result)


def GetMul(num1,num2):
    global result
    result = float(num1) * float(num2)
    result = float("{0:.2f}".format(result))
    Equals.delete(0,"end")
    Equals.insert(0,result)


def GetDiv(num1,num2):
    global result
    result = float(num1) / float(num2)
    result = float("{0:.2f}".format(result))
    Equals.delete(0,"end")
    Equals.insert(0,result)


def GetSub(num1,num2):
    global result
    result = float(num1) - float(num2)
    result = float("{0:.2f}".format(result))
    Equals.delete(0,"end")
    Equals.insert(0,result)


def GetBig(num1,num2):
    if(num1 > num2):
        Equals.delete(0,"end")
        Equals.insert(0,"TRUE")
    else:
        Equals.delete(0,"end")
        Equals.insert(0,"FALSE")
def GetSmall(num1,num2):
    if(num1 < num2):
        Equals.delete(0,"end")
        Equals.insert(0,"TRUE")
    else:
        Equals.delete(0,"end")
        Equals.insert(0,"FALSE")
root = Tk()
num1 = ""
num2 = ""
symbol = ""
before = True

root.title("Calculator")

menu = Menu(root)
quit = Menu(menu,tearoff = 0)
quit.add_command(label = "Quit",command = Quit)
menu.add_cascade(label = "Calculator",menu = quit)
Equals = Entry(root)
Equals.grid(row = 0,column = 1)

Button7 = Button(root,text = "7",width = 10)
Button7.bind("<Button-1>",Numbers7)
Button7.grid(row= 1,column = 0,)

Button8 = Button(root,text = "8",width = 20)
Button8.bind("<Button-1>",Numbers8)
Button8.grid(row= 1,column = 1,)

Button9 = Button(root,text = "9",width = 10)
Button9.bind("<Button-1>",Numbers9)
Button9.grid(row= 1,column = 2)

Button4 = Button(root,text = "4",width = 10)
Button4.bind("<Button-1>",Numbers4)
Button4.grid(row= 4,column = 0,)

Button5 = Button(root,text = "5",width = 20)
Button5.bind("<Button-1>",Numbers5)
Button5.grid(row= 4,column = 1,)

Button6 = Button(root,text = "6",width = 10)
Button6.bind("<Button-1>",Numbers6)
Button6.grid(row= 4,column = 2,)

Button1 = Button(root,text = "1",width = 10)
Button1.bind("<Button-1>",Numbers1)
Button1.grid(row= 7,column = 0,)

Button2 = Button(root,text = "2",width = 20)
Button2.bind("<Button-1>",Numbers2)
Button2.grid(row= 7,column = 1,)

Button3 = Button(root,text = "3",width = 10)
Button3.bind("<Button-1>",Numbers3)
Button3.grid(row= 7,column = 2,)

Buttonpl = Button(root,text = "+",width = 10)
Buttonpl.bind("<Button-1>",symbolpl)
Buttonpl.grid(row= 8,column = 0,)

Buttonmin = Button(root,text = "-",width = 20)
Buttonmin.bind("<Button-1>",symbolmin)
Buttonmin.grid(row= 8,column = 1,)

Buttondiv = Button(root,text = "/",width = 10)
Buttondiv.bind("<Button-1>",symboldiv)
Buttondiv.grid(row= 9,column = 0,)

Buttonmul = Button(root,text = "*",width = 10,)
Buttonmul.bind("<Button-1>",symbolmul)
Buttonmul.grid(row= 8,column = 2,)

Button0 = Button(root,text = 0,width = 10,)
Button0.bind("<Button-1>",Numbers0)
Button0.grid(row = 9, column = 2)

Buttoneq = Button(root,text = "=",width = 20)
Buttoneq.bind("<Button-1>",Ultimate)
Buttoneq.grid(row = 9,column = 1)

Buttonbig = Button(root,text = "C",width = 10)
Buttonbig.bind("<Button-1>",Clear)
Buttonbig.grid(row = 10,column = 0)

Buttondot = Button(root,text = ".",width = 20)
Buttondot.bind("<Button-1>",Numbersdot)
Buttondot.grid(row = 10,column = 1)

Buttonsmall = Button(root,text = "X",width = 10)
Buttonsmall.bind("<Button-1>",Quit)
Buttonsmall.grid(row = 10,column = 2)

root.config(menu = menu)


root.mainloop()
