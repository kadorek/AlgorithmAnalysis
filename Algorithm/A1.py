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
        h = abs(real(x) - near(x)) / real(x)
        print h;
        hatalar.append(h)
        pass

    #y ekseninin etiket değerinin ayarlanması
    plt.ylabel("Hata Payi")
    #x ekseninin etiketinin değerinin ayarlanması
    plt.xlabel("n")  
    # hesaplanan n sayıları ve bunlara karşılık gelen sürelerin(sn.  cinsinden)
    # kalınlığı 2 piksel çizgi kullanarak grafiğin çizimi
   
    plt.plot(nler, hatalar,linewidth=2)   
    # çizinlen grafiğin gösterimi
    plt.show()
    # grafiğin eksenlerinin başlangıç ve bitiş değerlerinin ayarlanması
    plt.axis([1,len(nler),0,2])
    # çalışan programın tüm işlemleri bitirdikten sonra ekranda birden
    # kaybolmaması için giriş kodu
    input()


    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))