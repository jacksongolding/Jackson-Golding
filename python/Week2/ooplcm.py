class lcm:
  def __call__(self, x, y):
    if (x>y):
      n = x
    else:
      n = y
    while (True):
      if (n % x == 0 and n % y == 0):
        break
      n = n + 1
    return n

def ooplcmTest():
  x = 12
  y = 8
  lcm_of = lcm()
  LCM = lcm_of(x,y)
  print("The lowest common multiple of 12 and 8 is: ", LCM)

  x = 5
  y = 6
  LCM = lcm_of(x,y)
  print("The lowest common multiple of 5 and 6 is: ", LCM)

  x = 9
  y = 15
  LCM = lcm_of(x,y)
  print("The lowest common multiple of 9 and 15 is: ", LCM)
  