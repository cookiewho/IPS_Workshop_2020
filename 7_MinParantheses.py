def minAddToMakeValid(S):
  stack = []
  for x in S:
    if x == "(":
      stack.append(x)
    if x == ")":
      try:
        if(stack[-1] != ")" ):
          stack.pop()
        else:
          stack.append(x)
      except:
        stack.append(x)
  return len(stack)
sampleInput = '())'
print(minAddToMakeValid(sampleInput))
'''
NO STACK SOLUTION
def minAddToMakeValid(S):
  left = 0
  right = 0
  for parenthese in S:
    if parenthese == "(":
      left += 1
    else:
      if left:
        left-=1
      else:
        right += 1
  return left + right
'''