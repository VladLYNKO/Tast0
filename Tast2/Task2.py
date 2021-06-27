Çàãîðàþùèé Ñâèíîáðàç, [23.06.21 18:18]
from tkinter import *
import math
v=[]
l=[]
class Main(Frame):
    def init(self, root):
        super(Main, self).init(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 25, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=23, y=67)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2",
            "cos","sin","tan","ctg",
            "log","ln", "%", "bin"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",font=("Times New Roman", 15),command=com).place(x=x, y=y,width=115,height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):

        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "cos":
            self.formula = str(math.cos(eval(self.formula)))
        elif operation == "sin":
            self.formula = str(math.sin(eval(self.formula)))
        elif operation == "tan":
            self.formula = str(math.tan(eval(self.formula)))
        elif operation == "ln":
            self.formula = str(math.log1p(eval(self.formula)))
        elif operation == "log":
            self.formula = str(math.log(eval(self.formula)))
        elif operation == "ctg":
            self.formula = str(math.cos (eval(self.formula)) / math.sin (eval(self.formula)))
        elif operation == "bin":
            self.formula = str(bin(eval(self.formula)))
        elif operation == "=":
            if '%' in self.formula:
                print(self.formula)
                a = float(self.formula.split('%')[0])
                print(a)
                b = float(self.formula.rsplit('%', 1)[-1])
                print(b)
                print(a, b)
                self.formula = str((a / 100) * b)
            else:
             self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if name__ == '__main':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("666x999")
    root.title("Äÿäüêî Ðàõ³âíèê")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
    
    
    
    
    
    
    Друга версія
    
    from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("SHUBHULATOR")

bar = Entry(root,width=22,font=("Ubuntu",18,"normal"),fg="blue",bg="Pale Turquoise")
bar.place(x=5,y=3)

X = 75
Y = 75

###################################################################################################

def insert(num):
    bar['fg']="blue"
    text = bar.get()
    if (text.split() == []) and (num=="/" or num=="*" or num==")"):
        num = ''
        
    elif (text.endswith('*')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()
    elif (text.endswith('/')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()
    elif (text.endswith('+')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()
    elif (text.endswith('-')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()

    elif (text.endswith('.')) and (num=="." or num=="+" or num=="-" or num=="/" or num=="*"):
        num=''
    bar.insert(END,num)

def BackSpace():
    bar['fg']="blue"
    try:
        text = bar.get()
        l = list(text)
        l.pop()
        Text = ""
        for i in range(len(l)):
            Text += l[i]
        bar.delete(0,END)
        bar.insert(0,Text)
    except:
        None
        
def Delete():
    bar['fg']="blue"
    bar.delete(0,END)

def BracketCheck():
    text = str(bar.get())
    Text = list(text)
    a=0
    for i in range(len(Text)):
        if Text[i] == "(":
            a+=1
    b=0
    for i in range(len(Text)):
        if Text[i] == ")":
            b+=1
    Add = a-b
    return Add

def Answer():
    text = str(bar.get())

    Add = BracketCheck()
    if Add>0:
        bar.insert(END,Add*")")
    
    else:
        try:
            answer = eval(text)
            Delete()
            bar.insert(0,answer)
            bar['fg'] = "forestgreen"
        except:
            bar['fg'] = "red"

###################################################################################################

n1 = Button(root,text="1",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("1"))
n1.place(x=0,y=Y+20)

n2 = Button(root,text="2",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("2"))
n2.place(x=X,y=Y+20)

n3 = Button(root,text="3",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("3"))
n3.place(x=2*X,y=Y+20)

n4 = Button(root,text="4",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("4"))
n4.place(x=0,y=(2*Y)+20)

n5 = Button(root,text="5",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("5"))
n5.place(x=X,y=(2*Y)+20)

n6 = Button(root,text="6",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("6"))
n6.place(x=2*X,y=(2*Y)+20)

n7 = Button(root,text="7",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("7"))
n7.place(x=0,y=(3*Y)+20)

n8 = Button(root,text="8",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("8"))
n8.place(x=X,y=(3*Y)+20)

n9 = Button(root,text="9",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("9"))
n9.place(x=2*X,y=(3*Y)+20)

n0 = Button(root,text="0",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light cyan",command=lambda:insert("0"))
n0.place(x=X,y=(4*Y)+20)

####################################################################################################

dot = Button(root,text=".",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="gray85",command=lambda:insert("."))
dot.place(x=0,y=(4*Y)+20)

equal = Button(root,text="=",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="green",command=Answer)
equal.place(x=2*X,y=(4*Y)+20)

####################################################################################################

mult = Button(root,text="X",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light green",command=lambda:insert("*"))
mult.place(x=3*X,y=Y+20)

div = Button(root,text="/",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light green",command=lambda:insert("/"))
div.place(x=3*X,y=(2*Y)+20)

plus = Button(root,text="+",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light green",command=lambda:insert("+"))
plus.place(x=3*X,y=(3*Y)+20)

minus = Button(root,text="-",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="light green",command=lambda:insert("-"))
minus.place(x=3*X,y=(4*Y)+20)

#####################################################################################################

AC = Button(root,text="AC",font=("Courier New",16,"bold"),padx = 14,pady = 6,bd = 4,bg="light yellow",command=Delete)
AC.place(x=0,y=Y-35)

back = Button(root,text=u"\u2190",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="light yellow",command=BackSpace)
back.place(x=X,y=Y-35)

Open = Button(root,text="(",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="light yellow",command=lambda:insert("("))
Open.place(x=2*X,y=Y-35)

Close = Button(root,text=")",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="light yellow",command=lambda:insert(")"))
Close.place(x=3*X,y=Y-35)

######################################################################################################

root.mainloop()
