def fizzbuzz(n):
  for curr in range(1,n+1):
    if curr % 3 == 0 and curr % 5 == 0:
      print("fizzbuzz")
    elif curr % 3 == 0:
      print("fizz")
    elif curr % 5 == 0:
      print ("buzz")
    else:
      print(curr)

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)