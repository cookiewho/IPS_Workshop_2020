def backspace(string):
  stack = []
  for char in string:
    if char == "#":
      try:
        stack.pop()
      except:
        continue
    else:
      stack.append(char)
  return "".join(stack)
  
def backspaceCompare(String1, String2):
  """
  :type String1: str
  :type String2: str
  :rtype: bool
  """
  s = backspace(String1)
  t = backspace(String2)
  print (s + " " + t)
  return s == t

W = "y#fo##f"
L = "y#f#o##f"
S0 = "ab#"
T0 = "ab#"
S1 = "ab#c"
T1 = "ad#c"
S2 = "ab##"
T2 = "c#d#"
S3 = "a##c"
T3 = "#a#c"
S4 = "a#c" 
T4 = "b"
print(backspaceCompare(W, L))
# print(backspaceCompare(S0, T0)) #true
# print(backspaceCompare(S1,T1))  #true
# print(backspaceCompare(S2,T2))  #true
# print(backspaceCompare(S3,T3))  #true
# print(backspaceCompare(S4,T4))  #false
