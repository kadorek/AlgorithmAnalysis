import operator
import sys
import matplotlib.pyplot as plt
from random import randint


class Point(object):
    
    def __init__(self, x,y):
        self.X = x
        self.Y = y

    def IsTheSame(self,p):
        return self.X == p.X and self.Y == p.Y

    def Yazdir(self):
        return "P(%s,%s)" % (self.X,self.Y)



TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

xMin = 50
yMin = 50
xMax = 250
yMax = 250
n = 10
points = [];
hull=[];

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)


def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
        hull.pop()
    # We check that hull[-1] != r to handle degenerate cases (ie. multisets)
    if not hull or hull[-1] != r:
    hull.append(r)
    return hull


def convex_hull(points):
    """Returns points on convex hull of an array of points in CCW order."""
    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    # We don't include the first or last point when extending l.
    l.extend(u[i] for i in xrange(1, len(u) - 1))
    return l

def main():
    while(len(points) < n):
        p = Point(randint(xMin,xMax),randint(yMin,yMax))       
        if len([a for a in points if a.IsTheSame(p)]) > 0:
            continue
        points.append(p)
    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))