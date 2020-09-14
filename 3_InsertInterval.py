def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  ans = []
  i = -1
  for i, x in enumerate(intervals):
    if x[1] <  newInterval[0]:
      ans.append(x)
    elif x[0] > newInterval[1]:
      i -= 1
      break
    else:
      newInterval[0] = min(newInterval[0], x[0])
      newInterval[1] = max(newInterval[1], x[1])
  return ans + [newInterval] + intervals[i+1:]
  '''
  WAS ABLE TO MERGE MOST TEST CASES BUT DID NOT ACCOUNT FOR ITEMS
  THAT WERE LESS COMPLETLY LESS THAN THE NEXT ELEMENT AND RESULTED
  IN A FEW ERRORS. COULD BEFIXED WITH MORE CONDITIONALS, BUT WOULD
  BE BAD PRACTTICE
  
  first = False
  x = 0
  while x < len(intervals):
    if not first:
      if intervals[x][0] >= newInterval[0]:
        intervals[x][0] = newInterval[0]
        first = True
        print('nice')
      elif intervals[x][1] >= newInterval[0]:
        first = True
        print('nice')
    if first:
      if newInterval[1] <= intervals[x][1]:
        return intervals
      elif x+1 < len(intervals):
        if newInterval[1] >= intervals[x+1][0]:
          if newInterval[1] <= intervals[x+1][1] :
            intervals[x][1] = intervals[x+1][1]
            intervals.pop(x+1)
            return intervals
          else:
            intervals.pop(x+1)
            x -= 1
        else:
          intervals[x][1] = newInterval[1]
          return intervals
      else:
        intervals[x][1] = newInterval[1]
        return intervals
    x+=1
  intervals.append(newInterval)
  return intervals
  '''