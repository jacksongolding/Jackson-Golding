import math

def sqrt():
  num = float(input(" Enter a number: "))
  sqRoot = math.pow(num, 0.5)
  # determines the square root of given value
  print("The square root of a given number {0} = {1}".format(num, sqRoot)) 
  # prints the square root