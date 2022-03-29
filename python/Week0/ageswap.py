def swapValue(x,y):
  if x > y:
    temp = x 
    x = y
    y = temp
  return x,y

def swap(x,y):
  print("Original", x, y)
  x,y = swapValue(x,y)
  print("New", x, y)
  print(" ")

def swapTest():
  x = input("First Number; ")
  y = input("Second Number; ")
  swap(x,y)

