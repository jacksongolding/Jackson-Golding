import math

def cubrt():
  num = float(input(" Enter a number: "))
  cubeRoot = math.pow(num, 1/3)
  # determines the cube root of given value
  print("The cube root of a given number {0} = {1}".format(num, cubeRoot)) 
  # prints the cube root