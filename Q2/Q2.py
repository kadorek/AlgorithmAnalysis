﻿import sys
import timeit
from math import *
from matplotlib import pyplot as plt
import operator



nler = [100000,1000000,10000000,100000000,10000000000]


def main():
    indicators=["r.","g,","b<","c>","mv","y^","k1","r2","r3","g4","b8","yo"]
    zamanlar = {}   
    for t in nler:
        for x in range(1,13):        
            zamanlar["f"+str(x)] = globals()["f"+str(x)]([t]) 
        sorted_zamanlar= sorted(zamanlar.items(),key=operator.itemgetter(1))
        print " n : %d" %(t)
        for x in sorted_zamanlar:
            print( " %(doc)s  : %(zaman).30f " %{'doc':globals()[x[0]].__doc__,'zaman':x[1]})
        lines=[]
        indicatorIndex=0
        plt.figure(figsize=(10,10))     
        for x in zamanlar:
            line= plt.plot([t],zamanlar[x],indicators[indicatorIndex],label=globals()[x].__doc__)   
            indicatorIndex+=1
            lines.append(line);
            pass   
        plt.legend(loc="upper right") 
        plt.ylabel("Zaman(~ms)")
        plt.xlabel("n=%d"%(t))

    plt.show()
    plt.axis([1,100000,0,10])

    input()
    pass




#n^5*lnn
def f1(degerler):
    """ n^5*lnn """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,5) * log(x,e)
        z=timeit.default_timer() - t
        pass

    return z

    pass

#n^0.5
def f2(degerler):
    """ n^0.5 """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,0.5) 
        z=timeit.default_timer() - t
        pass

    return z

    pass

#n*log10(n)
def f3(degerler):
    """ n*log10(n) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(x,10)
        z=timeit.default_timer() - t
        pass

    return z
    pass


#n*ln(n^5)
def f4(degerler):
    """ n*ln(n^5) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(pow(x,5),e)
        z=timeit.default_timer() - t
        #z.append(timeit.default_timer() - t)
        pass

    return z
    pass


#n
def f5(degerler):
    """ n """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x
        z=timeit.default_timer() - t
        #z.append(timeit.default_timer() - t)
        pass

    return z
    pass



#n^(ln4)
def f6(degerler):
    """ n^(ln4) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,log(4,e))
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#1
def f7(degerler):
    """ 1 """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = 1
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#n*ln(n)
def f8(degerler):
    """ n*ln(n) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(x,e)
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass

#n^2*(ln(n))
def f9(degerler):
    """ n^2*(ln(n)) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,2) * log(x,e)
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass

#n^3
def f10(degerler):
    """ n^3 """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,3)
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#n^2
def f11(degerler):
    """ n^2 """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,2)
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass

#n^(log2(4))
def f12(degerler):
    """ n^(log2(4)) """
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,log(4,2))
        z=timeit.default_timer() - t
        #        z.append(timeit.default_timer() - t)
        pass
    return z
    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))


