class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)
p = Point() # Instantiate an object of type Point
q = Point()        
print(p.x, p.y, q.x, q.y)
p.x = 3
p.y = 4
print(p.y)
print(p.x)
print("(x={1}, y={0})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y

p = Point(3, 4)
print(p.to_string())