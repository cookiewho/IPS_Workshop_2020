def fast_trailing_zero_factorial(n):
  n = (n//5)
  n+= (n//5)
  return n

# print("Enter number")
# n = int(input())
# print("The number of trailing zeroes is " + str(fast_trailing_zero_factorial(n)))