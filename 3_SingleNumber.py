def single_number(integers):
  integers.sort()
  for x in range(0,len(integers),2):
    try:
      if integers[x] != integers[x+1]:
        return integers[x]
    except:
        return integers[x]     
      
print(single_number([4,1,2,1,2]))