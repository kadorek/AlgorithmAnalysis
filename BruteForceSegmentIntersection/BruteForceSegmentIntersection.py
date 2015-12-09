

import sys
from random import randint
from PIL import Image,ImageDraw,ImageFont


class Point(object):
    
    def __init__(self, x,y):
        self.X=x;
        self.Y=y

    def IsTheSame(self,p):
        return self.X==p.X and self.Y==p.Y

    def Yazdir(self):
        return "P(%s,%s)"%(self.X,self.Y)

class Segment(object):
    def __init__(self, p1,p2):
        self.P1=p1;
        self.P2=p2;
    def IsTheSame(self,s):
        return (self.P1.IsTheSame(s.P1) and self.P2.IsTheSame(s.P2)) or (self.P2.IsTheSame(s.P1) and self.P1.IsTheSame(s.P2))
    def Yazdir(self):
        return "S[{0},{1}]".format(self.P1.Yazdir(),self.P2.Yazdir())



xMax=200;
yMax=200;
xMin=0;
yMin=0;
n=3;
segments=[]

def CCW(p1, p2, p3):
    return (p2.X - p1.X)*(p3.Y - p1.Y) - (p2.Y - p1.Y)*(p3.X - p1.X)

def IsIntersect(s1,s2):
    ccw1=CCW(s1.P1,s1.P2,s2.P1)*CCW(s1.P1,s1.P2,s2.P2)
    ccw2=CCW(s2.P1,s2.P2,s1.P1)*CCW(s2.P1,s2.P2,s1.P2)
    return ccw1<0 and ccw2<0

def main():

    im = Image.new('RGBA', (400, 400), (255, 255, 255, 0)) 
    draw = ImageDraw.Draw(im) 
    font = ImageFont.truetype("arial.ttf", 7)
    kesisenOlduMu=False
    for x in range(n):
        pA =Point(randint(xMin,xMax),randint(yMin,yMax))
        pB=Point(randint(xMin,xMax),randint(yMin,yMax))
        while(pA.IsTheSame(pB)):
            pA =Point(randint(xMin,xMax),randint(yMin,yMax))
            pB=Point(randint(xMin,xMax),randint(yMin,yMax))
        s=Segment(pA,pB)
        segments.append(s)
        draw.line((s.P1.X,s.P1.Y,s.P2.X,s.P2.Y),fill=0);
        draw.text((s.P1.X+5,s.P1.Y+5),s.Yazdir(),fill=128, font=font)

    im.show()

    for x in range(len(segments)):
        s1=segments[x]
        for k in range(len(segments)):
            s2=segments[k]
            if s1.IsTheSame(s2):
                continue
            if IsIntersect(s1,s2):
                print s1.Yazdir()
                print s2.Yazdir()
                print "----------------------------------"
                kesisenOlduMu=True               
                break

    if kesisenOlduMu==False:
        print u"Kesişen olmadı."
    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))




