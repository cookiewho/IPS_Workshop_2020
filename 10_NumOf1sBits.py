def count_set_bits(num):
  count = 0
  while num >0:
    num &= num -1
    count+=1
  return count
print(count_set_bits(200))

#4294967295