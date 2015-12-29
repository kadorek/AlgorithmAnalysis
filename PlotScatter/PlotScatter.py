import sys
from matplotlib  import pyplot as plt


#Noktlar� tan�mlamak �zere kullan�lan s�n�f yap�s�
class Point(object):
    
    def __init__(self, x,y):
        self.X = x
        self.Y = y

    def IsTheSame(self,p):
        return self.X == p.X and self.Y == p.Y

    def Yazdir(self):
        return "P(%s,%s)" % (self.X,self.Y)



def main():
    p1=Point(10,20);
    p2=Point(30,40);
    p3=Point(15,55);

    plt.scatter([10,30,15],[20,40,55]);
    plt.plot([10,30],[20,40],"r");
    plt.plot([30,15],[40,55],"g")
    plt.show();
    input();

    pass




    

if __name__ == "__main__":
    sys.exit(int(main() or 0))



