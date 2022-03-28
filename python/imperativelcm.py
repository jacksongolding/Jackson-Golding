def lcm(x,y):
  if (x>y):
    n = x
  else:
    n = y
  while (True):
    if (n % x == 0 and n % y == 0):
      break
    n = n + 1
  return n

def lcmTest():
  print("The lowest common multiple of 12 and 8 is: ", lcm(12,8))
  print("The lowest common multiple of 5 and 6 is: ", lcm(5,6))
  print("The lowest common multiple of 9 and 15 is: ", lcm(9,15))
  
  
  