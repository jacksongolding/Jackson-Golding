class factorial: 
  def __call__(self,n):
    if n==0 or n==1:
      return 1
    else:
      return n * self(n-1)

def factorialTest():
  factorial_of = factorial()
  print("factorial of 5: ", factorial_of(5))
  print("factorial of 3: ", factorial_of(3))
  print("factorial of 1: ", factorial_of(1))  