from math import sqrt, sin, cos, exp
from matplotlib import pyplot as plt

V0 = 70
th = .8
g = 10
m = 20
A = .7
Cd = .2
rho = 1.2
Vt = sqrt((2*m*g)/(rho*A*Cd))
t = 0
dt = 1/30

x, y = [0], [0]
while True:
    t += dt
    d = (1-exp(-g*t/Vt))
    x.append(((V0*Vt*cos(th))/g)*d)
    y.append((Vt/g)*(V0*sin(th)+Vt)*d-(Vt*t))
    if y[-1] < 0:
        y[-1] = 0
        break

print(f"Initial Speed: {V0}")
print(f"Angle of Release (Radians): {th}")
print(f"Gravitation: -{g}m/s^2")
print(f"Projectile Mass: {m}")
print(f"Cross Sectional Area: {A}")
print(f"Drag Coefficient: {Cd}")
print(f"Air Density: {rho}")
print(f"Terminal Velocity: {Vt}")
plt.plot(x,y)