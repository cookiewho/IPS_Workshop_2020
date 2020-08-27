'''
Given an integer, print "Fizz" if it's divisible by 3, print "Buzz"
if divisible by 5, "FizzBuzz" if divisible by both 3 & 5, "Not fizz
or buzz" otherwise (without the quotes).
'''
a = int(input())
s = ""
if  a%3 == 0: 
  s+=("Fizz")
if a % 5 == 0: 
  s+=("Buzz")
if len(s) > 0:
  print (s)
else:
  print("Not fizz or buzz")