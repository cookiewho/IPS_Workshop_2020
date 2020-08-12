def nlp_calculator(statement):
  statement = statement.split()
  a = word_to_num([statement[1]])
  b = word_to_num([statement[-1]])
  nums_ans = translator[statement[0]](a,b)
  return num_to_word(nums_ans)
  
def word_to_num(words):
  words = "".join(words)
  if words in word_dict:
    return word_dict[words]
  words = words.split("-")
  num = 0
  for word in words:
    if word in word_dict:
      num += word_dict[word]
  return num

def num_to_word(num):
  ans = ""
  if str(num)[0] == '-':
    ans+="negative "
    num *= -1
  temp = num
  while num:
    if temp in num_dict:
      ans += num_dict[temp]
      num -= temp
    else:
      remainder = num%10
      temp = num - remainder
      ans += num_dict[temp] + "-"
      num = temp = remainder
  return ans
  
def add(a,b):
  return a + b
  
def subtract(a,b):
  return b - a
  
def multiply(a,b):
  return a * b
  
def divide(a, b):
  return round(a/b)
  
translator = {
  "add": add,
  "subtract":subtract,
  "multiply": multiply,
  "divide":divide,
}
word_dict = {
  "zero":0,
  "one": 1,
  "two":2,
  "three":3,
  "four":4,
  "five":5,
  "six":6,
  "seven":7,
  "eight":8,
  "nine":9,
  "ten":10,
  "eleven":11,
  "twelve":12,
  "thirteen":13,
  "fourteen":14,
  "fifteen":15,
  "sixteen":16,
  "seventeen":17,
  "eighteen":18,
  "nineteen":19,
  "twenty":20,
  "thirty":30,
  "fourty":40,
  "fifty":50,
  "sixty":60,
  "seventy":70,
  "eighty":80,
  "ninety":90,
  "one-hundred":100
}
num_dict = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10:"ten",
  11:"eleven",
  12:"twelve",
  13:"thirteen",
  14:"fourteen",
  15:"fifteen",
  16:"sixteen",
  17:"seventeen",
  18:"eighteen",
  19:"nineteen",
  20:"twenty",
  30:"thirty",
  40:"fourty",
  50:"fifty",
  60:"sixty",
  70:"seventy",
  80:"eighty",
  90:"ninety",
}
test1 ="subtract thirty-four from seventy"
print(nlp_calculator(test1))