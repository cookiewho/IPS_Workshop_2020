def wave_array(integers):
  integers.sort()
  for x in range(len(integers)-1):
    if x %2 == 0:
      if integers[x] <= integers[x+1]:
        temp = integers[x+1]
        integers[x+1] = integers[x]
        integers[x] = temp
    else:
      if integers[x] >= integers[x+1]:
        temp = integers[x+1]
        integers[x+1] = integers[x]
        integers[x] = temp
  return integers
print(wave_array([1, 2, 3, 4]))