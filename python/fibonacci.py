def fibonacci(n):
  if n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacciTest():
  try:
    n = int(input("Enter a number: "))
    if n < 0:
      raise ValueError
    for n in range(n + 1):
      print(fibonacci(n))
  except ValueError:
    print("Invalid number. Must be a whole number greater than   or equal to 0")
    
  
