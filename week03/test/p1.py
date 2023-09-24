def getFactorial(n):
  if n == 0:
    return 1
  else:
    return n * getFactorial(n - 1)

print(getFactorial(5))