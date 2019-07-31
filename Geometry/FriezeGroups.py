import matplotlib.pyplot as plt
import numpy as np


## Add explanations and stuff


points = np.array([[0,0],[.5,0],[.5,1.5],[1,1.5],[1,2],[0,2]])


fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
for i in range(10):
    ps = points + [i*1.25,0]
    p = plt.Polygon(ps,fc='r')
    plt.gca().add_patch(p)
plt.axis('scaled')



fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
ptr1 = [.5,0,1,0]
ptr2 = [1,1,-1,-1]
ptr3 = [1,-1,1,-1]
cls = ['r','b','y','g']
ctr = 0
for i in range(20):
    ctr += ptr1[i%4]
    ps = points * [ptr2[i%4],ptr3[i%4]]
    ps = ps + [ctr*1.75,0]
    p = plt.Polygon(ps,fc=cls[i%4])
    plt.gca().add_patch(p)
plt.axis('scaled')



fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
cls = ['r','y']
for i in range(6):
    ps = points * [(-1)**(i%2),1]
    ps = ps + [i*2,0]
    p = plt.Polygon(ps,fc=cls[i%2])
    plt.gca().add_patch(p)
plt.axis('scaled')



fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
ptr1 = [.5,.5,1,.5]
ptr2 = [1,1,-1,-1]
ptr3 = [1,-1,1,-1]
cls = ['r','orange','y','purple']
ctr = 0
for i in range(12):
    ctr += ptr1[i%4]
    ps = points * [ptr2[i%4],ptr3[i%4]]
    ps = ps + [ctr*1.75,0]
    p = plt.Polygon(ps,fc=cls[i%4])
    plt.gca().add_patch(p)
plt.axis('scaled')



fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
ps = points[:]
ptr = [0,0,1,0]
cls = ['r','b']
for i in range(26):
    ps *= [1,(-1)**(i%2)]
    ps = ps + [(1.5)*ptr[i%4],0]
    p = plt.Polygon(ps,fc=cls[i%2])
    plt.gca().add_patch(p)
plt.axis('scaled')


fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
cls = ['r','orange']
for i in range(10):
    ps = points + [i*1.25,0]
    ps *= [1,(-1)**(i%2)]
    p = plt.Polygon(ps,fc=cls[i%2])
    plt.gca().add_patch(p)
plt.axis('scaled')



fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes()
cls = ['r','g']
for i in range(10):
    ps = points * [(-1)**(i%2),(-1)**(i%2)]
    ps = ps + [i*1.25,0]
    p = plt.Polygon(ps,fc=cls[i%2])
    plt.gca().add_patch(p)
plt.axis('scaled')

