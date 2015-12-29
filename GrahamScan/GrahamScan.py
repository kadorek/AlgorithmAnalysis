import operator
import sys
import matplotlib.pyplot as plt
from random import randint


#Noktları tanımlamak üzere kullanılan sınıf yapısı
class Point(object):
    
    def __init__(self, x,y):
        self.X = x
        self.Y = y

    def IsTheSame(self,p):
        return self.X == p.X and self.Y == p.Y

    def Yazdir(self):
        return "P(%s,%s)" % (self.X,self.Y)

def egim(p1,p2):
    return (p2.Y-p1.Y)/(p2.X-p1.X);
    pass

# 3 noktanın CCW değerinin hesaplanması
def CCW(p1, p2, p3):
    return (p2.X - p1.X) * (p3.Y - p1.Y) - (p2.Y - p1.Y) * (p3.X - p1.X)

#iki noktayı açısal olarak karşılaştırır
def karsilastir(p1,p2):
    d = CCW(p0,p1,p2)

    if d == 0:
        return -1 if (uzaklik(p0, p2) >= uzaklik(p0, p1)) else 1
    return -1 if d < 0 else 1

def EgimeGoreKarsilastir(p1,p2):
    e1=egim(p0,p1);
    e2=egim(p0,p2);
    if e1<e2:
        return 1;
    if e2<e1:
        return -1;
    else:
        return -1 if (uzaklik(p0, p2) >= uzaklik(p0, p1)) else 1
    
def uzaklik(p1,p2):
    return (p1.X - p2.X) * (p1.X - p2.X) + (p1.Y - p2.Y) * (p1.Y - p2.Y)

p0 = Point(1,1)
xMin = 50
yMin = 50
xMax = 250
yMax = 250
n = 10
points = []
def main():
    #noktalar oluşturuldu
    while(len(points) < n):
        p = Point(randint(xMin,xMax),randint(yMin,yMax))       
        if len([a for a in points if a.IsTheSame(p)]) > 0:
            continue
        points.append(p)
    
    print u"Rasgele üretilen noktalar : "   
    print    [a.Yazdir() for a in  points]
    returnedHull = graham_hull(points)
    print " -------------------------- "
    print u"Convex hull noktaları : "   
    print [a.Yazdir() for a in returnedHull]
    
    x_list = [a.X for a in points]
    y_list = [a.Y for a in points]    
    plt.scatter(x_list,y_list)
    for x in range(len(points)):
        plt.annotate(points[x].Yazdir(),
             xy=(points[x].X, points[x].Y), xycoords='data',
             xytext=(+5, +10), textcoords='offset points', fontsize=10)
    for x in range(len(returnedHull)):
        next=x+1;
        if next==len(returnedHull):
            next=0;
        p1=returnedHull[x];
        p2=returnedHull[next];
        plt.plot([p1.X,p2.X],[p1.Y,p2.Y],"r");


        pass
    
    plt.show()






    input()
    pass

def graham_hull(pointList):
    hull = []
    sortedPoints = sorted(pointList,key=lambda a:a.X)
    print u"noktalar x e gore sıralandı : ";    
    print [a.Yazdir() for a in sortedPoints]

    hull.append(sortedPoints[0])
    p0 = hull[0]
    acisalSirali = sorted(sortedPoints[1:],karsilastir)
    
    print u"noktalar açısal sıralandı : ";    
    print [a.Yazdir() for a in acisalSirali]
    uygunlar = []

    for x in range(len(acisalSirali)):
        while((x < n - len(acisalSirali) - 1) and CCW(hull[0],acisalSirali[x],acisalSirali[x + 1]) == 0):
            x+=1
            pass
        uygunlar.append(acisalSirali[x])
        pass

    if len(uygunlar) < 3:
        return 
    print u"noktalar uygunluk sıralandı : ";    
    print [a.Yazdir() for a in acisalSirali]
    hull.append(uygunlar[0])
    hull.append(uygunlar[1])

    for x in range(3,len(uygunlar)):
        while(CCW(hull[-2],hull[-1],uygunlar[x]) >= 0 and  len(hull)>2):
            hull.pop()
        hull.append(uygunlar[x])
        pass
    return hull
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))