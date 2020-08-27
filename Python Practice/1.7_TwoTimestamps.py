# Read an integer:
timestamp1 = 0
a1 = int(input())
timestamp1 += a1*60*60
a1 = int(input())
timestamp1 += a1*60
timestamp1 += int(input())

timestamp2 = 0
b1 = int(input())
timestamp2 += b1*60*60
b1 = int(input())
timestamp2 += b1*60
timestamp2 += int(input())

print(timestamp2 - timestamp1)
