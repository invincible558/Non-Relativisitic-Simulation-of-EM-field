from tkinter import *
from PIL import ImageTk,Image


menu = Tk()
menu.title('choose the simulation you want to do')

def openCalculator():
    root = Tk()
    root.title("Simple Calculator")
    ef = Entry(root, width=35, borderwidth=5)
    ef.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    
    #e.insert(0, "")
    def efupdate(exp):
        current=ef.get()
        ef.delete(0, END)
        ef.insert(0, str(current) + exp)
    
    def button_click(exp):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + exp)
            
    def operation_click(op):
        current = e.get()
        print(e.get())
        e.delete(0, END)
        if op == "+" or op == "-" or op == "/" or op == "*" or op == "^" or op == ")" :
            efupdate(str(current)+op)
        if op == "sin" or op == "cos" or op == "tan":
            efupdate(op+"("+str(current))
        if op == "(":
            efupdate(op)
        e.delete(0,END)
        
    def main_clear():
        ef.delete(0,END)
        
    def button_clear():
        e.delete(0, END)

    def button_equal():
        global finalexpstr
        finalexpstr = str(ef.get())+str(e.get())
        print(finalexpstr)


    # Define Buttons

    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click("0"))
    button_add = Button(root, text="+", padx=40, pady=20,command = lambda: operation_click("+"))
    button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=40, pady=20, command=button_clear)
    button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: operation_click("-"))
    button_multiply = Button(root, text="", padx=40, pady=20, command=lambda: operation_click(""))
    button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: operation_click("/"))
    button_sin = Button(root, text="Sin", padx=40, pady=20, command=lambda: operation_click("sin"))
    button_cos = Button(root, text="Cos", padx=40, pady=20, command=lambda: operation_click("cos"))
    button_tan = Button(root, text="Tan", padx=40, pady=20, command=lambda: operation_click("tan"))
    button_power = Button(root, text="^", padx=40, pady=20, command=lambda: operation_click("^"))
    button_x = Button(root, text="x", padx=40, pady=20, command=lambda: button_click("x"))
    button_y = Button(root, text="y", padx=40, pady=20, command=lambda: button_click("y"))
    button_z = Button(root, text="z", padx=40, pady=20, command=lambda: button_click("z"))
    button_t = Button(root, text="t", padx=40, pady=20, command=lambda: button_click("t"))
    button_ob = Button(root, text="(", padx=40, pady=20, command=lambda: operation_click("("))
    button_cb = Button(root, text=")", padx=40, pady=20, command=lambda: operation_click(")"))
    button_mainclear = Button(root, text="Clear main", padx=40, pady=20, command=main_clear)
    # Put the buttons on the screen

    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)

    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)

    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)

    button_0.grid(row=5, column=0)
    button_clear.grid(row=5, column=1, columnspan=1)
    button_add.grid(row=6, column=0)
    button_equal.grid(row=5, column=2, columnspan=1)

    button_subtract.grid(row=6, column=1)
    button_multiply.grid(row=6, column=2)
    button_divide.grid(row=7, column=0)

    button_sin.grid(row=7,column=1)
    button_cos.grid(row=7,column=2)
    button_tan.grid(row=8,column=0)
    button_power.grid(row=8,column=1)
    button_x.grid(row=8,column=2)
    button_y.grid(row=9,column=0)
    button_z.grid(row=9,column=1,columnspan=1)
    button_t.grid(row=9,column=2,columnspan=1)
    button_ob.grid(row=10,column=0)
    button_cb.grid(row=10,column=1)
    button_mainclear.grid(row=10,column=2)
    root.mainloop()

def openRelativistic():
    return


def openNonRelativistic():
    nrelroot = Tk()
    nrelroot.title("Ch0ose Values")
    lnrelB = Label(nrelroot, text="Enter values for B").grid(row=0, column=0,columnspan=3)
    bnrelBx = Button(nrelroot, text="Enter Eqn for Bx", command=openCalculator).grid(row=1, column=0)
    bnrelBy = Button(nrelroot, text="Enter Eqn for By", command=openCalculator).grid(row=1, column=1)
    bnrelBz = Button(nrelroot, text="Enter Eqn for Bz", command=openCalculator).grid(row=1, column=2)
    lnrelE = Label(nrelroot, text="Enter values for E").grid(row=2, column=0,columnspan=3)
    bnrelEx = Button(nrelroot, text="Enter Eqn for Ex", command=openCalculator).grid(row=3, column=0)
    bnrelEy = Button(nrelroot, text="Enter Eqn for Ey", command=openCalculator).grid(row=3, column=1)
    bnrelEz = Button(nrelroot, text="Enter Eqn for Ez", command=openCalculator).grid(row=3, column=2)
    lnrel = Label(nrelroot, text="Enter initial Veclocity in x, y & z direction in the boxes").grid(row=4, column=0,columnspan=3)
    enrel1 = Entry(nrelroot, width=10, borderwidth=5).grid(row=5, column=0, padx=10, pady=10)
    enrel1 = Entry(nrelroot, width=10, borderwidth=5).grid(row=5, column=1, padx=10, pady=10)
    enrel1 = Entry(nrelroot, width=10, borderwidth=5).grid(row=5, column=2, padx=10, pady=10)
    
b1 = Button(menu, text="Relativistic", command=openRelativistic).grid(row=0, column=0,columnspan = 2)

b2 = Button(menu, text="Non Relativistic", command=openNonRelativistic).grid(row=1, column=0,columnspan = 2)



mainloop()
