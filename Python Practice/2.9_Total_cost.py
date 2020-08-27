# Read an integer:
a = int(input())
b = int(input())
c = int(input())
# Print a value:
a *= c
b *= c
if b >= 100:
  a += b//100
  b%= 100
print(str(a) + " " + str(b))
