import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
ds = pd.read_csv("D:\Lenovo\Documents\GitHub\Sem4Exps\ML\exp1.csv")
print(ds.shape)
print(ds.head())

x=np.array(ds["X"])
y=np.array(ds["Y"])
x_mn=x.mean()
y_mn=y.mean()

nr=0 #numerator
dr=0 #denominator
for i in range(len(x)):
  nr+=(x[i]-x_mn)*(y[i]-y_mn)
  dr+=(x[i]-x_mn)*(x[i]-x_mn)
m=nr/dr
c = y_mn - m*x_mn
print(m,c)

yp=[] #predicted y values array
for i in range(len(x)):
  a = m*x[i] + c
  yp.append(a)
yp

plt.scatter(x,y)
plt.plot(x,yp)
plt.grid(True)
plt.show()

lr = 0.001
m=0
c=0
epochs=100
n=len(x)

dm=0
dc=0

for j in range(epochs):
  #dm=0
  #dc=0
  for j in range(n):
    yp=m*x[i]+c
    dm+=(y[i]-yp)*x[i]
    dc+=(y[i]-yp)
    dm*=float((-1)*2/n)
    dc*=float((-1)*2/n)
    m-=(lr*dm)
    c-=(lr*dc)

print(m,x)

y_p=[]
for i in range(5):
  y_c = m*x[i] + c
  y_p.append(y_c)
print(y_p)

plt.scatter(x,y)
plt.plot(x,y_p)
plt.grid(True)
plt.show()