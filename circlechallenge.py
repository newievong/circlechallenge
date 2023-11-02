import math
class Circle:
   def __init__(self, radius):
       self.radius = radius


   def calculate_diameter(self):
       diameter = self.radius * 2
       return f'Diameter: {diameter}'
   def calculate_circumference(self):
       circumference = self.radius * 2 * math.pi
       return f'Circumference: {circumference}'


   def calculate_area(self):
       area = math.pi * self.radius ** 2
       return f'Area: {area}'


   def grow(self):
       self.radius = self.radius * 2


   def get_radius(self):
       return self.radius




while True:
    radius = float(input("Welcome to the Circle Tester. Enter a radius up to two decimal points: "))

    while radius < 0:
	    radius = int(input('That is not a valid value. Please enter a positive number, up to two decimal points: '))


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





