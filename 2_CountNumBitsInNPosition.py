# Read two integers a & b:
input_value = input()
values = input_value.split();
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])
n = int(values[4])


mask = 1 << n
count = 0
for x in range(4):
  if int(values[x]) & mask:
    count += 1
print(count)
# Count the number of 1's in the nth lsb position
# in a, b, c and d and print it