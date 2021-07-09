from tkinter import *
from PIL import ImageTk,Image
import vpython
from vpython import *
import math
import numpy as np
from Equation import Expression

fEx = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fEy = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fEz = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBx = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBy = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBz = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])

choice = "rel"
origin=vector(0,0,0)
def make_axes(length):
    xaxis=arrow(pos=origin,axis=length*vector(1,0,0),shaftwidth=.9,headwidth=.9,color=color.red)
    yaxis=arrow(pos=origin,axis=length*vector(0,1,0),shaftwidth=.9,headwidth=.9,color=color.red)
    zaxis=arrow(pos=origin,axis=length*vector(0,0,1),shaftwidth=0.9,headwidth=.9,color=color.red)
    nxaxis=arrow(pos=origin,axis=length*vector(-1,0,0),shaftwidth=.9,headwidth=.9,color=color.red)
    nyaxis=arrow(pos=origin,axis=length*vector(0,-1,0),shaftwidth=.9,headwidth=.9,color=color.red)
    nzaxis=arrow(pos=origin,axis=length*vector(0,0,-1),shaftwidth=0.9,headwidth=.9,color=color.red)
def modifyB(x,y,z,t):
    return vector(fBx(x,y,z,t),fBy(x,y,z,t),fBz(x,y,z,t))

def modifya_nonrelativistic(V,x,y,z,t):
    return vector(V.y*fBz(x,y,z,t)-V.z*fBy(x,y,z,t)+fEx(x,y,z,t),-1*V.x*fBz(x,y,z,t)+V.z*fBx(x,y,z,t)+fEy(x,y,z,t),V.x*fBy(x,y,z,t)-V.y*fBx(x,y,z,t)+fEz(x,y,z,t))

def dotp(V,x,y,z,t):
    return V.x*fEx(x,y,z,t)+V.y*fEy(x,y,z,t)+V.z*fEz(x,y,z,t)

def modifya_relativistic(V,x,y,z,t,gamma):
    return vector(((-1*V.x/gamma)*dotp(V,x,y,z,t))+V.y*fBz(x,y,z,t)-V.z*fBy(x,y,z,t)+fEx(x,y,z,t),((-1*V.y/gamma)*dotp(V,x,y,z,t))-1*V.x*fBz(x,y,z,t)+V.z*fBx(x,y,z,t)+fEy(x,y,z,t),((-1*V.z/gamma)*dotp(V,x,y,z,t))+V.x*fBy(x,y,z,t)-V.y*fBx(x,y,z,t)+fEz(x,y,z,t))

def modifygamma(V):
    return (1/math.sqrt(1-(V.x**2+V.y**2+V.z**2)))

def simulate_nonrelativsitic():
    g1=graph(title='Position vs time ')
    pos_curve_x=gcurve(color=color.red)
    pos_curve_y=gcurve(color=color.green)
    pos_curve_z=gcurve(color=color.blue)
    
    g2=graph(title = 'Magnetic Field vs Time')
    pos_B=gcurve(color=color.red)
    c=canvas(background=color.black,width=1300,height=720)
    obj=sphere(canvas=c,pos=vector(0,0,0),radius=0.5,make_trail=True)
    make_axes(100)
    dt=0.00001 
    time=0
    a=modifya_nonrelativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time)
    B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
    while (time<8):
        rate(1/dt)
        time+=dt
       
        a=modifya_nonrelativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time)
        B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
        obj.pos.x+=V.x*dt
        obj.pos.y+=V.y*dt
        obj.pos.z+=V.z*dt
        V.x+=a.x*dt
        V.y+=a.y*dt
        V.z+=a.z*dt
        pos_curve_x.plot(time,obj.pos.x)
        pos_curve_y.plot(time,obj.pos.y)
        pos_curve_z.plot(time,obj.pos.z)
        pos_B.plot(time,B.z)

def simulate_relativistic():
    pos_curve=gcurve(color=color.red)
    c=canvas(background=color.black,width=1500,height=500)
    obj=sphere(canvas=c,pos=vector(0,0,0),radius=0.5,make_trail=True,texture={'file':textures.stucco})
    make_axes(100)
    dt=0.0001 
    time=0
    gamma=modifygamma(V)
    dtau=gamma*dt
    a=modifya_relativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time,gamma)
    B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
    while (time<10):
        rate(8000)
        time+=dt
        gamma=modifygamma(V)
        dtau=gamma*dt
        a=modifya_relativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time,gamma)
        B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
        obj.pos.x+=V.x*dtau
        obj.pos.y+=V.y*dtau
        obj.pos.z+=V.z*dtau
        V.x+=a.x*dtau
        V.y+=a.y*dtau
        V.z+=a.z*dtau
        pos_curve.plot(time,obj.pos.x)
def create_menu():
    menu = Tk()
    menu.title('Particle Simulator')
   
    def openCalculator(x):
        root = Tk()
        root.title("Simple Calculator")
        l1=Label(root, text="     Final eqn:      ").grid(row=0, column=0)
        ef = Entry(root, width=35, borderwidth=5)
        ef.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        l1=Label(root, text="Press = for finalizing the equation ,initial value is set as 0").grid(row=0, column=4,columnspan = 3)
        l3=Label(root, text="Value to be inserted:").grid(row=1, column=0)
        e = Entry(root, width=35, borderwidth=5)
        e.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        l1=Label(root, text="For further info on how to insert input read the slides").grid(row=1, column=4,columnspan = 3)
        
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
            global fEx,fEy,fEz,fBx,fBy,fBz
            finalexpstr = str(ef.get())+str(e.get())
            if x == "Bx":
                fBx = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "By":
                fBy = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Bz":
                fBz = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ex":
                fEx = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ey":
                fEy = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ez":
                fEz = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            print(x+"="+str(fBz))
            root.destroy()

        def button_back():
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current)[:-1])
            
        # Define Buttons

        button_1 = Button(root, text="  1  ", padx=40, pady=20, command=lambda: button_click("1"))
        button_2 = Button(root, text="  2  ", padx=40, pady=20, command=lambda: button_click("2"))
        button_3 = Button(root, text="  3  ", padx=40, pady=20, command=lambda: button_click("3"))
        button_4 = Button(root, text="  4  ", padx=40, pady=20, command=lambda: button_click("4"))
        button_5 = Button(root, text="  5  ", padx=40, pady=20, command=lambda: button_click("5"))
        button_6 = Button(root, text="  6  ", padx=40, pady=20, command=lambda: button_click("6"))
        button_7 = Button(root, text="  7  ", padx=40, pady=20, command=lambda: button_click("7"))
        button_8 = Button(root, text="  8  ", padx=40, pady=20, command=lambda: button_click("8"))
        button_9 = Button(root, text="  9  ", padx=40, pady=20, command=lambda: button_click("9"))
        button_0 = Button(root, text="  0  ", padx=40, pady=20, command=lambda: button_click("0"))
        button_add = Button(root, text="  +  ", padx=40, pady=20,command = lambda: operation_click("+"))
        button_equal = Button(root, text="  =  ",  command=button_equal,width = 10,height = 10)
        button_clear = Button(root, text="Clear",  command=button_clear,width = 10,height = 10)
        button_subtract = Button(root, text="  -  ", padx=40, pady=20, command=lambda: operation_click("-"))
        button_multiply = Button(root, text="  *  ", padx=40, pady=20, command=lambda: operation_click("*"))
        button_divide = Button(root, text="  /  ", padx=40, pady=20, command=lambda: operation_click("/"))
        button_sin = Button(root, text=" Sin ", padx=37, pady=20, command=lambda: operation_click("sin"))
        button_cos = Button(root, text=" Cos ", padx=36, pady=20, command=lambda: operation_click("cos"))
        button_tan = Button(root, text=" Tan ", padx=37, pady=20, command=lambda: operation_click("tan"))
        button_power = Button(root, text="  ^  ", padx=40, pady=20, command=lambda: operation_click("^"))
        button_x = Button(root, text="  x ", padx=40, pady=20, command=lambda: button_click("x"))
        button_y = Button(root, text="  y  ", padx=40, pady=20, command=lambda: button_click("y"))
        button_z = Button(root, text="  z  ", padx=40, pady=20, command=lambda: button_click("z"))
        button_t = Button(root, text="  t  ", padx=40, pady=20, command=lambda: button_click("t"))
        button_ob = Button(root, text="  (  ", padx=40, pady=20, command=lambda: operation_click("("))
        button_cb = Button(root, text="  )  ", padx=40, pady=20, command=lambda: operation_click(")"))
        button_mainclear = Button(root, text="Clear main", command=main_clear,width = 10,height = 10 )
        button_backspace = Button(root, text="<-", command=button_back,width = 10,height = 10)
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
        button_clear.grid(row=2, column=6, rowspan=2)
        button_add.grid(row=2, column=3)
        button_equal.grid(row=4, column=7, rowspan=2)

        button_subtract.grid(row=2, column=4)
        button_multiply.grid(row=2, column=5)
        button_divide.grid(row=5, column=3)

        button_sin.grid(row=3,column=4)
        button_cos.grid(row=3,column=5)
        button_tan.grid(row=4,column=3)
        button_power.grid(row=3,column=3)
        button_x.grid(row=4,column=4)
        button_y.grid(row=4,column=5)
        button_z.grid(row=5,column=4)
        button_t.grid(row=5,column=5)
        button_ob.grid(row=5,column=1)
        button_cb.grid(row=5,column=2)
        button_mainclear.grid(row=2,column=7,rowspan=2)
        button_backspace.grid(row=4,column=6,rowspan = 2)
        root.mainloop()

    
        
    

    def openinputfield(sys):
        global choice
        choice =sys
            
            
        
        nrelroot = Tk()
        nrelroot.title("Choose Values")
        lnrelB = Label(nrelroot, text="Enter values for B").grid(row=0, column=0,columnspan=3)
        bnrelBx = Button(nrelroot, text="Enter Eqn for Bx", command=lambda: openCalculator("Bx")).grid(row=1, column=0)
        bnrelBy = Button(nrelroot, text="Enter Eqn for By", command=lambda: openCalculator("By")).grid(row=1, column=1)
        bnrelBz = Button(nrelroot, text="Enter Eqn for Bz", command=lambda: openCalculator("Bz")).grid(row=1, column=2)
        lnrelE = Label(nrelroot, text="Enter values for E").grid(row=2, column=0,columnspan=3)
        bnrelEx = Button(nrelroot, text="Enter Eqn for Ex", command=lambda: openCalculator("Ex")).grid(row=3, column=0)
        bnrelEy = Button(nrelroot, text="Enter Eqn for Ey", command=lambda: openCalculator("Ey")).grid(row=3, column=1)
        bnrelEz = Button(nrelroot, text="Enter Eqn for Ez", command=lambda: openCalculator("Ez")).grid(row=3, column=2)
        lnrel = Label(nrelroot, text="Enter initial Velocity in x, y & z direction in the boxes").grid(row=4, column=0,columnspan=3)
        enrel1 = Entry(nrelroot, width=10, borderwidth=5)
        enrel1.grid(row=5, column=0, padx=10, pady=10)
        enrel2 = Entry(nrelroot, width=10, borderwidth=5)
        enrel2.grid(row=5, column=1, padx=10, pady=10)
        enrel3 = Entry(nrelroot, width=10, borderwidth=5)
        enrel3.grid(row=5, column=2, padx=10, pady=10)
        def setv():
            V.x=int(enrel1.get())
            V.y=float(enrel2.get())
            V.z=float(enrel3.get())
           
        bnrelV = Button(nrelroot, text="confirm values for V: ", command = setv).grid(row=6, column=1)

    def simulate():
        menu.destroy()
        
    l=Label(menu, text="Choose the type of motion").grid(row=0, column=0,columnspan = 2)    
    b1 = Button(menu, text="Relativistic", command=lambda: openinputfield("rel")).grid(row=1, column=0,columnspan = 2)
    l2= Label(menu,text=": Velocity will be choosen in terms of c,and speed of light will be considered as unit").grid(row=1,column=3,columnspan = 4)
    l3= Label(menu,text=": Velocity chosen in m/s: ").grid(row=2,column=2,columnspan = 3)
    b2 = Button(menu, text="Non Relativistic", command=lambda: openinputfield("nonrel")).grid(row=2, column=0,columnspan = 2)
    b3 = Button(menu, text="Simulate!", command=simulate).grid(row=3, column=0,columnspan = 2)


    mainloop()

B=vector(0,0,0)
V=vector(0,0,0)
E=vector(0,0,0)    
create_menu()
print("V is "+ str(V))
print("fbx is "+ str(fBx))
print("fby is "+ str(fBy))
print("fbz is "+ str(fBz))
print("fex is "+ str(fEx))
print("fey is "+ str(fEy))
print("fez is "+ str(fEz))
if choice == "rel":
    simulate_relativistic()
if choice == "nonrel":
    simulate_nonrelativsitic()