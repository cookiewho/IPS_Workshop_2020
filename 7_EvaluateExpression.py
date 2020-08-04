def evaluate_expression(expression):
  stack = []
  for num_op in expression:
    if num_op == "+":
      stack.append(int(stack.pop()) + int(stack.pop()))
    elif num_op == "-":
      num1 = int(stack.pop())
      num2 = int(stack.pop())
      stack.append(num2 - num1)
    elif num_op == "*":
      stack.append(int(stack.pop()) * int(stack.pop()))
    elif num_op == "/":
      num1 = int(stack.pop())
      num2 = int(stack.pop())
      stack.append(num2 // num1)
    else:
      stack.append(num_op)
  return (stack[0])
expression = ["3", "4", "+", "5", "-"]
print(evaluate_expression(expression))