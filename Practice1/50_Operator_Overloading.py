class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

pnt1= Point(1,4)
pnt2= Point(3,6)
print(pnt1+pnt2)
