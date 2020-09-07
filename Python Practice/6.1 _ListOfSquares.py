'''
For a given integer N, print all the squares of positive integers
where the square is less than or equal to N, in ascending order.
'''
a = int(input())
x = 1
while(x*x <= a):
  print(x*x, end = " ")
  x+=1
