#Question 1
from math import sqrt

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    @property
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    @classmethod
    def from_tuple(cls, t):
        v1, v2 = t[0], t[1]
        return cls(v1, v2)
        
v1 = Vector2D(3,4)
print(v1)
print(v1.magnitude)
print(Vector2D.from_tuple((5,6)))

#Question 4

class CountDown():
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 1:
            raise StopIteration
        current = self.start
        self.start -=1
        return current
        
        
cd = CountDown(5)

for num in cd:
    print(num)

#Question 5
def countdown_gen(start):
    while start >= 1:
        yield start
        start -= 1

for num in countdown_gen(7):
    print(num)