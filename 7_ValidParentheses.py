def valid(parentheses):
  stack = []
  for x in parentheses:
    if x == '(':
      stack.append(x)
    elif x == ')' and len(stack)>0 and stack[-1] == '(':
      stack.pop()
    elif x == '[':
      stack.append(x)
    elif x == ']' and len(stack)>0 and stack[-1] == '[':
      stack.pop()
    elif x == '{':
      stack.append(x)
    elif x == '}' and len(stack)>0 and stack[-1] == '{':
      stack.pop()
    else:
      return 0
  if len(stack) == 0:
    return 1
  else:
    return 0
'''
NO STACK SOLUTION
  lpar = rpar = lbracket = rbracket = lcurl = rcurl = 0
        for char in A:
            if char == '(':
                lpar+= 1
            elif char == ')':
                if lpar:
                    lpar-=1
                else:
                    rpar += 1
            elif char == '[':
                lbracket+= 1
            elif char == ']':
                if lbracket:
                    lbracket-=1
                else:
                    rbracket += 1
            elif char == '{':
                lcurl += 1
            elif char == '}':
                if lcurl:
                    lcurl-=1
                else:
                    rcurl += 1
        if (lpar + rpar + lbracket + rbracket + lcurl + rcurl) == 0:
            return 1
        else:
            return 0
'''

test1 = '()[]{}'
test2 = '{()()}'
test3 = '(]([)]'
test4 = '[]()]'
print(valid(test1))
print(valid(test2))
print(valid(test3))
print(valid(test4))
