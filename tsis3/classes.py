class MyString:
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s)


# a = MyString()
# a.getString()
# a.printString()


class Shape:
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)


# C = Shape()
# C.area()
# B = Square(4)
# B.area()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


# B = Rectangle(4, 5)
# B.area()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def show(self):
        print(f"my coordinates: {self.x}, {self.y}")

    def dist(self, oth):
        dx = self.x - oth.x
        dy = self.y - oth.y
        return (dx ** 2 + dy ** 2) ** (1 / 2)


# A = Point(1, 2)
# B = Point(2, 3)
# A.move(4, 4)
# A.show()
# print(A.dist(B))

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, x):
        assert x > 0
        self.balance += x

    def withdraw(self, x):
        assert x <= self.balance
        self.balance -= x


# A = Account("Amanbol", 500)
# # # A.withdraw(1000)
# A.deposit(1000)
# # A.withdraw(1000)
#
# A.deposit(5)
# print(A.balance)

L = [3, 4, 2]
primes = filter(lambda a: all(a % w for w in range(2, a)), L)
for x in primes:
    print(x, end = " ")