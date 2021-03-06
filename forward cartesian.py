import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import msvcrt
from matplotlib.widgets import Slider


A_l0=0
x0=np.array([1,0,0])
y0=np.array([0,1,0])
z0=np.array([0,0,1])

def F_cartesian(d1,d2,d3):
    P0=0
    P1=P0+d1*y0
    P2=P1+d2*x0
    P3=P2+d3*z0
    return P0,P1,P2,P3
    
def I_cartesian(px,py,pz):
    d1=py;d2=px;d3=pz
    return d1,d2,d3


p0,p1,p2,p3=F_cartesian(10,10,10)
print(p0,p1,p2,p3)
d1,d2,d3=I_cartesian(p3[0],p3[1],p3[2])
print(d1,d2,d3)

x=[p0,p1[0],p2[0],p3[0]]
y=[p0,p1[1],p2[1],p3[1]]
z=[p0,p1[2],p2[2],p3[2]]

plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
l,=ax.plot(x, y, z, "o-",label='Cartesian Robot',mew=1)
ax.legend()
ax.set_xlim(-10,20)
ax.set_ylim(-10,20)
ax.set_zlim(  0,30)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
theta1= plt.axes([0.25, 0.1, 0.65, 0.03])
theta2= plt.axes([0.25, 0.05, 0.65, 0.03])
theta3= plt.axes([0.25, 0, 0.65, 0.03])
slider1= Slider(theta1, r'd1', 0,  10.0, valinit=0)
slider2= Slider(theta2, r'd2', 0,  10.0, valinit=0)
slider3= Slider(theta3, r'd3', 0,  10.0, valinit=0)
def update(val):
    for txt in ax.texts:
        txt.set_visible(False)
    s1 = slider1.val
    s2 = slider2.val
    s3 = slider3.val
    p0,p1,p2,p3=F_cartesian(s1,s2,s3)
    x=np.array([p0,p1[0],p2[0],p3[0]])
    y=np.array([p0,p1[1],p2[1],p3[1]])
    z=np.array([p0,p1[2],p2[2],p3[2]])
    l.set_xdata(x)
    l.set_ydata(y)
    l.set_3d_properties(z)
    for x, y, z in zip(x, y, z):
        label = '(%.2f, %.2f, %.2f)' % (x, y, z)
        ax.text(x, y, z, label)
    fig.canvas.draw_idle()

slider1.on_changed(update)
slider2.on_changed(update)
slider3.on_changed(update)
plt.show()
