import vpython
from vpython import *
import math
import numpy as np
origin=vector(0,0,0)
def make_axes(length):
    xaxis=arrow(pos=origin,axis=length*vector(1,0,0),shaftwidth=.9,headwidth=.9,color=color.red)
    yaxis=arrow(pos=origin,axis=length*vector(0,1,0),shaftwidth=.9,headwidth=.9,color=color.red)
    zaxis=arrow(pos=origin,axis=length*vector(0,0,1),shaftwidth=0.9,headwidth=.9,color=color.red)
    nxaxis=arrow(pos=origin,axis=length*vector(-1,0,0),shaftwidth=.9,headwidth=.9,color=color.red)
    nyaxis=arrow(pos=origin,axis=length*vector(0,-1,0),shaftwidth=.9,headwidth=.9,color=color.red)
    nzaxis=arrow(pos=origin,axis=length*vector(0,0,-1),shaftwidth=0.9,headwidth=.9,color=color.red)
def modifyB(time):
    return vector(2*time,2*time,2*time)

def modifya(V,B,E):
    return vector(V.y*B.z-V.z*B.y+E.x,-1*V.x*B.z+V.z*B.x+E.y,V.x*B.y-V.y*B.x+E.z)

def simulate_nonrelativsitic(obj,B,E,V):
    make_axes(100)
    dt=0.0001 
    time=0
    a=vector(V.y*B.z-V.z*B.y+E.x,-1*V.x*B.z+V.z*B.x+E.y,V.x*B.y-V.y*B.x+E.z)
    while (time<10):
        rate(8000)
        time+=dt
        B=vector(0,0,time)
        E=vector(0,0,0)
        obj.pos.x+=V.x*dt
        obj.pos.y+=V.y*dt
        obj.pos.z+=V.z*dt
        V.x+=a.x*dt
        V.y+=a.y*dt
        V.z+=a.z*dt
        a=modifya(V,B,E)
        pos_curve.plot(time,obj.pos.x)
pos_curve=gcurve(color=color.red)
c=canvas(background=color.black,width=1500,height=500)
obj=sphere(canvas=c,pos=vector(0,0,0),radius=0.5,make_trail=True,texture={'file':textures.stucco})
B=vector(0,0,1)
V=vector(10,0,1)
E=vector(0,1,0)
simulate_nonrelativsitic(obj,B,E,V)
