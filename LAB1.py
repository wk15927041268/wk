# coding:utf-8
import  os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
a0 = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
numb = 0#记录总个数
filename = 'magic04.txt'
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        numb += 1
        if not lines:
            break
            pass
        attr0_tmp, attr1_tmp, attr2_tmp, \
        attr3_tmp, attr4_tmp, attr5_tmp, \
        attr6_tmp, attr7_tmp, attr8_tmp, \
        attr9_tmp,attr = [i for i in lines.split(",")]
        a0.append(float(attr0_tmp))
        a1.append(float(attr1_tmp))
        a2.append(float(attr2_tmp))
        a3.append(float(attr3_tmp))
        a4.append(float(attr4_tmp))
        a5.append(float(attr5_tmp))
        a6.append(float(attr6_tmp))
        a7.append(float(attr7_tmp))
        a8.append(float(attr8_tmp))
        a9.append(float(attr9_tmp))
        pass
    pass


print sum(a0)/numb
print sum(a1)/numb
print sum(a2)/numb
print sum(a3)/numb
print sum(a4)/numb
print sum(a5)/numb
print sum(a6)/numb
print sum(a7)/numb
print sum(a8)/numb
print sum(a9)/numb

y = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
print  np.cov(y)
a=np.array(a0)
b=np.array(a1)
plt.plot(a,b,'bo')
plt.show()


data = a
mean = data.mean()
std = data.std()
def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
x = np.arange(-200,200,0.1)
y = normfun(x, mean, std)
plt.plot(x,y)
plt.hist(data, bins=10, rwidth=1, normed=True)
plt.title('data distribution')
plt.xlabel('data')
plt.ylabel('probability')
plt.show()


def variancefun(a):
    array = np.array(a)
    var = array.var()
    return var
print variancefun(a0)
print variancefun(a1)
print variancefun(a2)
print variancefun(a3)
print variancefun(a4)
print variancefun(a5)
print variancefun(a6)
print variancefun(a7)
print variancefun(a8)
print variancefun(a9)


def covfun(a):
    array = np.array(a)
    cov = np.cov(array)
    return cov
print covfun(a0)
print covfun(a1)
print covfun(a2)
print covfun(a3)
print covfun(a4)
print covfun(a5)
print covfun(a6)
print covfun(a7)
print covfun(a8)
print covfun(a9)



