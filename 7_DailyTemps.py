def dailyTemperatures(dailyTemps):
  stack = []
  for temp in range(len(dailyTemps)):
    count = 0
    found =False
    for lrgr_temp in range(temp+1,len(dailyTemps)):
      count+=1
      if dailyTemps[lrgr_temp] > dailyTemps[temp]:
        stack.append(count)
        found =True
        break
    if found == False:
      stack.append(0)
  return stack
sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))