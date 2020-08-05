def removeOuterParentheses(string):
  stack = []
  outer = False
  opened = 0
  for par in string:
    if outer == False and par == '(':
      outer = True
    elif par == ')' and opened == 0:
      outer = False
    elif par == '(':
      opened += 1
      stack.append(par)
    elif par == ')' and stack[-1] == '(':
      opened -= 1
      stack.append(par)
    else:
      opened -= 1
      stack.append(par)
  return "".join(stack)


sampleInput = "(()())(())"
sampleInput2 = "(()())(())(()(()))"
print(removeOuterParentheses(sampleInput))
print(removeOuterParentheses(sampleInput2))