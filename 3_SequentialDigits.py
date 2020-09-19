def sequentialDigits(low, high): # CANT GET TO 1000000000(TIME LIMIT EXCEEDED)
  ans = []
  s_low = str(low)
  s_high = str(high)
  temp = [int(x) for x in s_low]
  first = True
  while len(temp) <= len(s_high):
    y=0
    while y < len(temp):
      if (y == 0):
        if first:
          first = False
          y+=1
          continue
        else:
          temp[y] +=1
      else:
        t_val = temp[y-1]+1
        if t_val >= 10:# might cause issues
          temp=[0]*(len(temp)+1)
          temp[0] = 1
          first = True
          y = -1
        else:
          temp[y]=t_val
      '''
      PREVIOUS BODY, DID NOT ACCOUT FOR NUMS STARTING IN THE 10's OR NOT % 10 == 0
      if (temp[y] == 0):
        if y-1 == 0:
          temp[y-1] -=1
        temp[y] = temp[y-1] +1
        
      else:
        t_val = temp[y]+1
        if t_val >= 10:# might cause issues
          temp=[0]*(len(temp)+1)
          temp[0] = 1
          y = -1
        else:
          temp[y]=t_val
        '''
      y+=1
    sr = [str(i) for i in temp]
    sr = "".join(sr)
    if int(sr) < high:
      ans.append(int(sr))
    else:
      break
  return ans

'''
BELOW IS LEETCODE APPROVED, MADE WITH HELP
'''
def sequentialDigits2(low, high):
  ans = []
  queue = list(range(1,10))
  while queue:
    val = queue.pop(0)
    if low <= val <= high:
      ans.append(val)
    elif high < val:
      return ans
    last = val %10
    if last < 9:
      queue.append(val*10 +last +1)
  return ans

print(sequentialDigits(1000, 13000))
print(sequentialDigits2(10, 1000000000))