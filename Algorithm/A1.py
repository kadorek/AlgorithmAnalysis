import sys
from timeit import *
from math import *
from matplotlib import pyplot as plt



def  real(n):
    return n * n + 2 * n + 5
    pass


def near(n):
    return n * n
    pass


def main():
    nler = []
    hatalar = []

    for x in range(1000,1000000):
        nler.append(x)
        h = abs(real(x) - near(x)) / float(real(x))
        #print h
        hatalar.append(h)
        pass

    plt.ylabel("Hata Payi")
    plt.xlabel("n")  
   
    plt.plot(nler, hatalar,linewidth=2)   
    plt.show()
    plt.axis([1,len(nler),0,2])
    input()


    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))