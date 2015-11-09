# gerekli kütüphanelerin çağırımı
import sys
from matplotlib import pyplot as plt
import timeit
import math


#25. elemana kadar bulunabilmesi için limi 26
limit = 26
#n. elemanın bulunması için geçen sürenin sn. cinsinden tutmak için liste
zaman = []
#grafik üzerinde n sayısını göstermek için liste    
sayilar=[]
def main():
    # n sayısının her değerini bulmak için kullanılmak üzere döngü
   for x in range(1,limit):
       #sıradaki n. sayının hesaplanması için başlangıç zamanı
       start = timeit.default_timer()
       #bulunan n. sayının ekrana yazıdırılması için 
       print(fibonacci(x))
       # n. sayının bulunması için geçen sürenin hesabı ve bu  sürenin zaman listesine eklenmesi  
       zaman.append(timeit.default_timer() - start)
       # n değerinin listeye eklenmesi
       sayilar.append(x) 
   #y ekseninin etiket değerinin ayarlanması
   plt.ylabel("Zaman(sn)")
   #x ekseninin etiketinin değerinin ayarlanması
   plt.xlabel("n")  
   # hesaplanan n sayıları ve bunlara karşılık gelen sürelerin(sn. cinsinden) kalınlığı 2 piksel çizgi kullanarak grafiğin çizimi
   
   plt.plot(sayilar, logal(zaman),linewidth=2)   
   # çizinlen grafiğin gösterimi
   plt.show()
   # grafiğin eksenlerinin başlangıç ve bitiş değerlerinin ayarlanması
   plt.axis([1,30,0,2])
   # çalışan programın tüm işlemleri bitirdikten sonra ekranda birden kaybolmaması için giriş kodu
   input()
 

#öz yinelemeli yöntemle n. sıradaki fibonacci sayısını bulan metod
def   fibonacci(n):
    # n=1 değeri için şart
    if(n == 1):
        return 1
    #n=2 değeri için şart
    if(n == 2):
        return 1
    # öz yinelemeli şekilde metod çağırımının yapıldığı alan. bulunacak sıradaki sayıdan bir ve iki önceki sayı toplanır.
    return fibonacci(n - 1) + fibonacci(n - 2)
  
 
def logal(z):
    yeni=[]

    for x in z:
        yeni.append(math.log(x,2))
    return yeni;
     

if __name__ == "__main__":
    sys.exit(int(main() or 0))