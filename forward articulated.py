import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import msvcrt
from matplotlib.widgets import Slider


A_l0=0;A_l1=10;A_l2=10;A_l3=10
z0=np.array([0,0,1])

def rotate_z(theta):
    radian=m.radians(theta)
    return np.array([[m.cos(radian),-m.sin(radian),0],
                     [m.sin(radian), m.cos(radian),0],
                     [0            ,0             ,1]])

def rotate_y(theta):
    radian=m.radians(theta)
    return np.array([[ m.cos(radian),0,m.sin(radian)],
                     [0             ,1,            0],
                     [-m.sin(radian),0,m.cos(radian)]])

def F_articulated(theta_1,theta_2,theta_3):
    C20=np.dot(rotate_z(theta_1),rotate_y(theta_2))
    C30=np.dot(C20,rotate_y(theta_3))
    P0=0
    P1=P0+A_l0*z0
    P2=P1+A_l1*z0
    P3=P2+A_l2*np.dot(C20,z0)
    P4=P3+A_l3*np.dot(C30,z0)
    return P0,P1,P2,P3,P4
    
def I_articulated(px,py,pz):
    theta_1=m.atan2(py,px)
    r_square=m.pow(px,2)+m.pow(py,2)
    c=(r_square+m.pow(pz-A_l1,2)-m.pow(A_l2,2)-m.pow(A_l3,2))/(2*A_l2*A_l3)
    s=m.sqrt(1-m.pow(c,2))
    theta_3=m.atan2(s,c)
    theta_2=m.atan2(m.sqrt(r_square),pz-A_l1)-m.atan2(A_l3*s,A_l2+A_l3*c)
    return m.degrees(theta_1),m.degrees(theta_2),m.degrees(theta_3)

p0,p1,p2,p3,p4=F_articulated(0,0,0)
print(p0,p1,p2,p3,p4)
theta_1,theta_2,theta_3=I_articulated(p4[0],p4[1],p4[2])
print(theta_1,theta_2,theta_3)

x=[p0,p1[0],p2[0],p3[0],p4[0]]
y=[p0,p1[1],p2[1],p3[1],p4[1]]
z=[p0,p1[2],p2[2],p3[2],p4[2]]

plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
l,=ax.plot(x, y, z, "o-",label='Articulated Robot',mew=1)
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
slider1= Slider(theta1, r'$\theta_1$', -180,180.0, valinit=0)
slider2= Slider(theta2, r'$\theta_2$', -180,180.0, valinit=0)
slider3= Slider(theta3, r'$\theta_3$', -90,  90.0, valinit=0)
def update(val):
    for txt in ax.texts:
        txt.set_visible(False)
    s1 = slider1.val
    s2 = slider2.val
    s3 = slider3.val
    p0,p1,p2,p3,p4=F_articulated(s1,s2,s3)
    x=np.array([p0,p1[0],p2[0],p3[0],p4[0]])
    y=np.array([p0,p1[1],p2[1],p3[1],p4[1]])
    z=np.array([p0,p1[2],p2[2],p3[2],p4[2]])
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
