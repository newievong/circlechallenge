import math
class Circle:
   def __init__(self, radius):
       self.radius = radius


   def calculate_diameter(self):
       diameter = self.radius * 2.0
       return f'Diameter: {diameter}'

   def calculate_circumference(self):
       circumference = self.radius * 2.0 * math.pi
       return f'Circumference: {circumference}'


   def calculate_area(self):
       area = math.pi * (self.radius ** 2.0)
       return f'Area: {area}'


   def grow(self):
       self.radius = self.radius * 2.0


   def get_radius(self):
       return self.radius

def value_type(a):
    try:
        value = float(a)
        return 'float'
    except ValueError:
        return 'str'


while True:
    radius = input("Welcome to the Circle Tester. Enter a radius up to two decimal points: ")

    while value_type(radius) == 'str':
        print('Please select a number.')
        radius = input("Welcome to the Circle Tester. Enter a radius up to two decimal points: ")
    else:
        radius = float(radius)
        print("Calculating...")

    circle = Circle(radius)
    print(circle.calculate_diameter())
    print(circle.calculate_circumference())
    print(circle.calculate_area())

    choice = input("Would you like to see your circle grow? Enter 'y' or 'n': ")
    while choice == 'y':
        circle.grow()
        print(circle.calculate_diameter())
        print(circle.calculate_circumference())
        print(circle.calculate_area())
        choice = input("Would you like to see your circle grow? Enter 'y' or 'n': ")

    if choice == 'n':
        print("Goodbye!")
        break

    else:
        print("This is not a valid input. Please try again.")
        break






