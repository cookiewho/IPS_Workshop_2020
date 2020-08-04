def k_backspace(inputString):
  stack = []
  for x in inputString:
    if (x == "<"):
      stack.pop()
    else:
      stack.append(x)
  return "".join(stack)

# don't forget to actually call your answer's function!
testInput = 'a<bc<'
actualOutput = k_backspace(testInput)
print(actualOutput)