import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
plt.axis([-2,2,-2,2])

def mxbline(mb=[0,0],x=[-2,2]):
    y = [mb[0]*x[0]+mb[1],mb[0]*x[1]+mb[1]]
    plt.plot(x,y)
    
    
def intersect(m1,b1,m2,b2):
    x = (b2-b1)/(m1-m2)
    y = x*m1+b1
    return x,y


mb1 = [2,.5]
mb2 = [-3,1]
mxbline(mb1)
mxbline(mb2)

a = intersect(mb1[0],mb1[1],mb2[0],mb2[1])
plt.plot(a[0],a[1],'ko')
print(a)
