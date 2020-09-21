'''
Brute Force solution, time limit exceeded once we reach upper bounds
def uniquePaths(m, n):
  count = 0
  def recurr(m, n, x, y, count):
    if x== n-1 and y == m-1:
      return count+1
    else:
      if(x+1) < n:
        count = recurr(m, n, x+1, y, count)
      if(y+1) < m:
        count = recurr(m, n, x, y+1, count)
      return count
  return recurr(m, n, 0,0, count)
'''
#LEETCODE APPROVED, WITH SOME HELP
def uniquePaths2(m, n):
  if m == 1 or n == 1:
    return 1
  ans = [1]*n
  for x in range(m-1):
    for y in range(n):
      if y == 0:
        ans[y] = 1
      else:
        ans[y] += ans[y-1]
  return ans[-1]

print(uniquePaths2(23,12))

