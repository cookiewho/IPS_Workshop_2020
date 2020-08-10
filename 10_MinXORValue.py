def min_xor_value(num):
  num.sort()
  min_num = num[-1]
  for x in range(len(num)-1):
    if (num[x] ^ num[x+1]) < min_num:
      min_num = num[x] ^ num[x+1]
  return min_num

print(min_xor_value([0, 2, 5, 7]))