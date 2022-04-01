import math

def square():
  
  num = float(input(" Enter a number: "))
  square = math.pow(num, 2.0)
  # determines the square of given value
  print("The square of a given number {0} = {1}".format(num, square)) 
  # prints the square