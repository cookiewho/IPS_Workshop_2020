'''
everyone must get at least 1 candy, and if someone has a score greater than their
left OR right, they have to have more than their neighbor
'''
def min_candies(line):
  increasing = []
  decreasing = []
  award = 0
  def count(inc_dec, line):
    num = 1
    for x in range(len(line)):
      if ((x+1) < len(line)):
        if  line[x] < line[x+1]:
          inc_dec.append(num)
          num +=1
        else:
          inc_dec.append(num)
          num = 1
      else:
        inc_dec.append(num)
  count(increasing, line)
  count(decreasing, line[::-1])
  for x in range(len(line)):
    award += max(increasing[x], decreasing[len(decreasing) - x -1])
  return award

  
print(min_candies([85, 90, 95, 85, 80, 75, 73, 72, 71, 73]))
print(min_candies([90, 95, 85, 80, 75, 83]))
