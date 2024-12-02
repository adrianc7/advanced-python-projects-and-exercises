
class Rectangle:
    def __init__(self, length, width ):
        self.length =  length
        self.width = width


    def area(self):
        return self.length * self.width


# Instance creation using the dimensions 5 by 3 for length and width

rectangle = Rectangle(5,3) 
print(f'The area of this rectangle is: {rectangle.area()}')