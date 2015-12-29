import operator
import sys
from random import randint
from matplotlib import pyplot as plt


#Noktları tanımlamak üzere kullanılan sınıf yapısı
class Point(object):
    
    def __init__(self, x,y):
        self.X=x;
        self.Y=y

    def IsTheSame(self,p):
        return self.X==p.X and self.Y==p.Y

    def Yazdir(self):
        return "P(%s,%s)"%(self.X,self.Y)

##Kullanılabilecek nokta uzayını belitmek için sınırlamalar.
xMax=400;
yMax=400;
xMin=0;
yMin=0; 
############
#nokta  adedi
n=15;
# 3 noktanın CCW değerinin hesaplanması
def CCW(p1, p2, p3):
    return (p2.X - p1.X)*(p3.Y - p1.Y) - (p2.Y - p1.Y)*(p3.X - p1.X)

def main():
    points=[];
    while(len(points)<n):
        p=Point(randint(xMin,xMax),randint(yMin,yMax));
        for x in points:
            if x.IsTheSame(p):
                continue;
        points.append(p);
    
    print u"Rasgele üretilen noktalar : ";   
    print    [a.Yazdir() for a in  points];
    returnedHull=convexhull(points);
    print " -------------------------- "
    print u"Convex hull noktaları : ";   
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



    input();
    pass

def convexhull(pointList):
    hull=[];
    orderedPointList=sorted(pointList,key=operator.attrgetter("X"));
    solPoint=orderedPointList[0];
    endPoint=Point(xMax+1,yMax+1);    
    hull.append(solPoint);
    while(endPoint.IsTheSame(hull[0])==False):
        if hull[0].IsTheSame(solPoint)==False:
            hull.append(solPoint);
        endPoint=pointList[0];
        for x in range(1,len(pointList)-1):
            if((endPoint==solPoint) or (CCW(solPoint,endPoint,pointList[x])<0)):
                endPoint=pointList[x];
        solPoint=endPoint;
        pass
    return hull;




if __name__ == "__main__":
    sys.exit(int(main() or 0))


