# Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
a = int(input())
b = int(input())
s = ""
for x in range(a, b+1):
  s += str(x) + " "
print (s)