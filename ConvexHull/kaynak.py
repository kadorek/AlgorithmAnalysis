from random  import randint




#Noktlar� tan�mlamak �zere kullan�lan s�n�f yap�s�
class Point(object):
    
    def __init__(self, x,y):
        self.X=x;
        self.Y=y

    def IsTheSame(self,p):
        return self.X==p.X and self.Y==p.Y

    def Yazdir(self):
        return "P(%s,%s)"%(self.X,self.Y)

xMax=200;
yMax=200;
n=10;
points =[];

# Graham Scan - Tom Switzer <thomas.switzer@gmail.com>

TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    """Returns points on convex hull of an array of points in CCW order."""
    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l


# 3 noktan�n CCW de�erinin hesaplanmas�
def CCW(p1, p2, p3):
    return (p2.X - p1.X)*(p3.Y - p1.Y) - (p2.Y - p1.Y)*(p3.X - p1.X)

while(len(points)<n):
    _x=randint(0,xMax);
    _y=randint(0,yMax);
    p=Point(_x,_y);
    if len([a for a in points if a.IsTheSame()])>0:
        continue;
    else:
        points.append(p);


sortedPoints=sorted(key=lambda a : a.Y);

