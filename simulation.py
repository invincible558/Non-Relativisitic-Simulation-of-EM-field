from tkinter import *
from PIL import ImageTk,Image
import vpython
from vpython import *
import math
import numpy as np
from Equation import Expression

c= 3*(10**8)
fEx = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fEy = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fEz = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBx = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBy = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
fBz = Expression("0*x+0*y+0*z+0*t",["x","y","z","t"])
q=1
m=1
Ex="0"
Ey="0"
Ez="0"
Bx="0"
By="0"
Bz="0"
choice = "rel"
relchoice = ""
origin=vector(0,0,0)
def make_axes(length):
    xaxis=arrow(pos=origin,axis=length*vector(1,0,0),shaftwidth=.3,headwidth=.3,color=color.red)
    yaxis=arrow(pos=origin,axis=length*vector(0,1,0),shaftwidth=.3,headwidth=.3,color=color.red)
    zaxis=arrow(pos=origin,axis=length*vector(0,0,1),shaftwidth=0.3,headwidth=.3,color=color.red)
    nxaxis=arrow(pos=origin,axis=length*vector(-1,0,0),shaftwidth=.3,headwidth=.3,color=color.red)
    nyaxis=arrow(pos=origin,axis=length*vector(0,-1,0),shaftwidth=.3,headwidth=.3,color=color.red)
    nzaxis=arrow(pos=origin,axis=length*vector(0,0,-1),shaftwidth=0.3,headwidth=.3,color=color.red)
    
def modifyB(x,y,z,t):
    return vector(fBx(x,y,z,t),fBy(x,y,z,t),fBz(x,y,z,t))

def modifya_nonrelativistic(V,x,y,z,t):
    return vector(V.y*fBz(x,y,z,t)-V.z*fBy(x,y,z,t)+fEx(x,y,z,t),-1*V.x*fBz(x,y,z,t)+V.z*fBx(x,y,z,t)+fEy(x,y,z,t),V.x*fBy(x,y,z,t)-V.y*fBx(x,y,z,t)+fEz(x,y,z,t))

def dotp(V,x,y,z,t):
    return V.x*fEx(x,y,z,t)+V.y*fEy(x,y,z,t)+V.z*fEz(x,y,z,t)

def modifya_relativistic(V,x,y,z,t,gamma,force):
    if(force == "E"):
        return vector((q*fEx(x,y,z,t))/(m*gamma),0,0)
    if(force == "B"):
        return vector((q*fBz(x,y,z,t)*V.y)/(m*(gamma**2)),-1*(q*fBz(x,y,z,t)*V.x)/(m*(gamma**2)),0)

def modifygamma(V):
    return (1/math.sqrt(1-(V.x**2+V.y**2+V.z**2)))

def simulate_nonrelativsitic():
    g1=graph(title='Position vs time ')
    pos_curve_x=gcurve(color=color.red)
    pos_curve_y=gcurve(color=color.green)
    pos_curve_z=gcurve(color=color.blue)
    c=canvas(background=color.black,width=1500,height=500)
    obj=sphere(canvas=c,pos=vector(0,0,0),radius=0.5,make_trail=True,texture={'file':textures.stucco})
    
    make_axes(100)
    dt=10**(-5)
    time=0
    a=modifya_nonrelativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time)
    B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
    while (time<10):
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

def simulate_relativistic(force):
    pos_curve=gcurve(color=color.red)
    c=canvas(background=color.white,width=1500,height=500)
    obj=sphere(canvas=c,pos=vector(0,0,0),radius=1,make_trail=True,color=color.green)
    c2=canvas(background=color.white,width=1500,height=500)
    obj2=sphere(canvas=c2,pos=vector(0,0,0),radius=0.5,make_trail=True,color=color.green)
    V2=V
    dt=10**(-6) 
    time=0
    tau=0
    gamma=modifygamma(V)
    dtau=gamma*dt
    a=modifya_relativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time,gamma,force)
    B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
    while (time<10 and (V.x**2+V.y**2+V.z**2)/(C**2) < 0.999999 ):
        rate(1/dt)
        time+=dt
        gamma=modifygamma(V)
        dtau=gamma*dt
        tau=tau+dtau
        a=modifya_relativistic(V,obj.pos.x,obj.pos.y,obj.pos.z,time,gamma,force)
        B=modifyB(obj.pos.x,obj.pos.y,obj.pos.z,time)
        obj.pos.x+=(V.x)*dt
        obj.pos.y+=(V.y)*dt
        obj.pos.z+=(V.z)*dt
        obj2.pos.x+=V2.x*dtau
        obj2.pos.y+=V2.y*dtau
        obj2.pos.z+=V2.z*dtau
        V.x+=a.x*dt
        V.y+=a.y*dt
        V.z+=a.z*dt
        V2.x+=a.x*dtau
        V2.y+=a.y*dtau
        V2.z+=a.z*dtau
        pos_curve.plot(tau,V2.x)
        print(V)

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
            global fEx,fEy,fEz,fBx,fBy,fBz,Ex,Ey,Ez,Bx,By,Bz
            
            finalexpstr = str(ef.get())+str(e.get())
            if x == "Bx":
                Bx=finalexpstr
                fBx = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "By":
                By=finalexpstr
                fBy = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Bz":
                Bz=finalexpstr
                fBz = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ex":
                Ex=finalexpstr
                fEx = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ey":
                Ey=finalexpstr
                fEy = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            if x == "Ez":
                Ez=finalexpstr
                fEz = Expression(finalexpstr+"+0*x+0*y+0*z+0*t",["x","y","z","t"])
            print(x+"="+str(finalexpstr+"+0*x+0*y+0*z+0*t"))
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
        choice = sys
        if(sys == "nonrel"):
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
            
            def setnrelv():
                V.x=float(enrel1.get())
                V.y=float(enrel2.get())
                V.z=float(enrel3.get())
                update_label()
                
                nrelroot.destroy()
               
            bnrelV = Button(nrelroot, text="confirm values for Fns ", command = setnrelv).grid(row=6, column=1)
        
        if(sys=="rel"):
            relroot = Tk()
            relroot.title("Choose one of the two systems")
            def system(c):
                global relchoice
                if(c=="Bz"):
                    relchoice="B"
                    openCalculator("Bz")
                if(c=="Ex"):
                    relchoice="E"
                    openCalculator("Ex")
                    
                    
            lrel = Label(relroot, text="Due to math constrains we can only choose 1-D coordinates for B or E ").grid(row=0, column=0,columnspan=5)
            brelB = Button(relroot, text="Enter 1D Eqn for B in z dirn ", command=lambda: system("Bz")).grid(row=1, column=0,columnspan=2)
            lrel2= Label(relroot, text="or").grid(row=1, column=2)
            brelF= Button(relroot, text="Enter 1D Eqn for E in x dirn ", command=lambda: system("Ex")).grid(row=1, column=3,columnspan=2)
            lrel = Label(relroot, text="Enter initial Velocity in x, y & z direction in the boxes in units of c").grid(row=2, column=0,columnspan=5)
            erel1 = Entry(relroot, width=10, borderwidth=5)
            erel1.grid(row=3, column=0, padx=10, pady=10,columnspan = 2)
            erel2 = Entry(relroot, width=10, borderwidth=5)
            erel2.grid(row=3, column=2, padx=10, pady=10)
            erel3 = Entry(relroot, width=10, borderwidth=5)
            erel3.grid(row=3, column=4, padx=10, pady=10,columnspan = 1)
            
            def setrelv():
                
                V.x=float(erel1.get())
                V.y=float(erel2.get())
                V.z=float(erel3.get())
                update_label()
                relroot.destroy()
               
            brelV = Button(relroot, text="confirm values for Fns ", command = setrelv).grid(row=4, column=0,columnspan=5)
        
    l=Label(menu, text="Choose values for charge & mass").grid(row=0, column=0,columnspan = 2)
    l1=Label(menu, text="charge: ").grid(row=1, column=0)
    e1 = Entry(menu, width=10, borderwidth=5)
    e1.grid(row=2,column = 0, padx=10, pady=10)
    l2=Label(menu, text="mass: ").grid(row=1, column=1)
    e2 = Entry(menu, width=10, borderwidth=5)
    e2.grid(row=2,column = 1, padx=10, pady=10)
    l3=Label(menu, text="Choose type of motion you want").grid(row=3, column=0,columnspan = 2)
    b1 = Button(menu, text="Relativistic", command=lambda: openinputfield("rel")).grid(row=4, column=0,columnspan = 1)
    b2 = Button(menu, text="Non Relativistic", command=lambda: openinputfield("nonrel")).grid(row=4, column=1,columnspan = 1)
    l3=Label(menu, text="Current values of E and B")
    l3.grid(row=5, column=0,columnspan = 2)
    l4=Label(menu, text="Bx:  "+Bx)
    l4.grid(row=6, column=0)
    l5=Label(menu, text="By:  "+By)
    l5.grid(row=7, column=0)
    l6=Label(menu, text="Bz:  "+Bz)
    l6.grid(row=8, column=0)
    l7=Label(menu, text="Ex:  "+Ex)
    l7.grid(row=9, column=0)
    l8=Label(menu, text="Ey:  "+Ey)
    l8.grid(row=10, column=0)
    l9=Label(menu, text="Ez:  "+Ez)
    l9.grid(row=11, column=0)
    l10=Label(menu, text="Current value of V")
    l10.grid(row=12, column=0,columnspan = 2)
    l11=Label(menu, text="Vx:  "+str(V.x))
    l11.grid(row=13, column=0)
    l12=Label(menu, text="Vy:  "+str(V.y))
    l12.grid(row=14, column=0)
    l13=Label(menu, text="Vz:  "+str(V.y))
    l13.grid(row=15, column=0)
    def update_label():
        l4.config(text="Bx:  "+Bx)
        l5.config(text="By:  "+By)
        l6.config(text="Bz:  "+Bz)
        l7.config(text="Ex:  "+Ex)
        l8.config(text="Ey:  "+Ey)
        l9.config(text="Ez:  "+Ez)
        l11.config(text="Vx:  "+str(V.x))
        l12.config(text="Vy:  "+str(V.y))
        l13.config(text="Vz:  "+str(V.z))
               
            
    def simulate():
        global q,m
        
        q=float(e1.get())
        m=float(e2.get())
        menu.destroy()
    l14=Label(menu, text=" ").grid(row=16, column=0)
    b3 = Button(menu, text="Simulate!", command=simulate,width = 20).grid(row=17, column=0,columnspan = 2)

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
    print(relchoice + "is" + str(relchoice))
    simulate_relativistic(relchoice)
if choice == "nonrel":
    simulate_nonrelativsitic()

