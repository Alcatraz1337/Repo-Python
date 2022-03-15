#已经写完,完美解决
from functools import reduce
import math
from scipy import integrate


def g(x):
    return pow(math.e,-(x*x/2))

def real(x):
    return 0.5+integrate.quad(g,0,x)[0]/math.sqrt(2*math.pi)

def f(x):
    n=99999 # 使用复化Simpson公式进行计算,划分区间个数
    a=0
    b=x
    h=(b-a)/n
    sumfk=0
    for i in range(1,n):
        sumfk=sumfk+g(a+i*h)
    Tn=(b-a)*(g(a)+2*sumfk+g(b))/(2*n)
    sumfk2=0
    for i in range(0,n):
        sumfk2=sumfk2+g(a+(i+0.5)*h)
    Sn=(b-a)*(g(a)+4*sumfk2+2*sumfk+g(b))/(6*n)

    return 0.5+Tn/math.sqrt(2*math.pi),0.5+Sn/math.sqrt(2*math.pi)

def problem():
    ''' 
    f(0.1k),k=1,2,3,....30,结果保留7位有效数字
    '''
    print(f'课本216页第13题的计算结果:')
    for k in range(1,31):
        #print(real(0.1*k))
        print(f'k={k},复化梯形公式求解f(0.1k)={round(f(0.1*k)[0],7)},复化Simpson公式求解f(0.1k)={round(f(0.1*k)[1],7)} ,f(0.1k)真实值:{round(real(0.1*k),7)}')

if __name__=='__main__':
    #print(real(0.1))
    problem()