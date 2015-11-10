import sys
import timeit
from math import *
from matplotlib import pyplot as plt


nler = range(1000,10000,85)



def main():


    zamanlar = {}
   
    for x in range(1,12):
        
        zamanlar["f"+str(x)] = globals()["f"+str(x)](nler) #  getattr(self,"f4")(nler)
        pass

    


    plt.ylabel("Zaman")
    plt.xlabel("n")     
    for x in zamanlar:
        plt.plot(nler,zamanlar[x])   
        pass    
    plt.show()
    plt.axis([1,len(nler),0,2])

    input()
    pass




#n^5*lnn
def f1(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,5) * log(x,e)
        z.append(timeit.default_timer() - t)
        pass

    return z

    pass

#n^0.5
def f2(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,0.5) 
        z.append(timeit.default_timer() - t)
        pass

    return z

    pass

#n*log10(n)
def f3(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(x,10)
        z.append(timeit.default_timer() - t)
        pass

    return z
    pass


#n*ln(n^5)
def f4(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(pow(x,5),e)
        z.append(timeit.default_timer() - t)
        pass

    return z
    pass


#n
def f5(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x
        z.append(timeit.default_timer() - t)
        pass

    return z
    pass



#n^(ln4)
def f6(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,log(4,e))
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#1
def f7(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = 1
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass
#n*ln(n)
def f8(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = x * log(x,e)
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass

#n^2*(ln(n))
def f9(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,2) * log(x,e)
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#n^3
def f10(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,3)
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass


#n^2
def f11(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,2)
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass

#n^(log2(4))
def f12(degerler):
    z = []
    for x in degerler:
        t = timeit.default_timer()
        v = pow(x,log(4,2))
        z.append(timeit.default_timer() - t)
        pass
    return z
    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))


