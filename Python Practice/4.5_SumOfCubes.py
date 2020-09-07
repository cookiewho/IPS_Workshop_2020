'''
For the given integer N calculate the following sum:
1³ + 2³ + ... + N³
'''

a = int(input())
tot=0
for x in range(a+1):
  tot += x**3
print(tot)
