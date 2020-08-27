# Read a float:
a = float(input())
# Print a value:
digits = [x for x in str(a)]
found = False
for x in digits:
  if found == True:
    print(x)
    break
  if x == ".":
    found = True
  
