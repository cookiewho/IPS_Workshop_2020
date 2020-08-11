def reverse_bits(num):
  ###ORIGINAL SOLUTION###
  num = str(bin(num))
  rev = "0b"
  for x in num[::-1]:
    if x == 'b':
      break
    else:
      rev += x
  for y in range(34-len(rev)):
    rev += '0'
  return int(rev,2)
'''
###SOLUTION WITH HELP###
  num = int(num)
  bits = 32
  rev = 0
  while num>0:
    current = (num &1)
    bits -=1
    current = current << bits
    rev |= current
    num >>=1
  return rev
'''
'''
###SOLUTION WITH HELP AND OPTIMIZATION###
  num = int(num)
  bits = 32
  rev = 0
  while num>0:
    bits -=1
    rev |= (num &1)<< bits
    num >>=1
  return rev
'''

n = 6
print(reverse_bits(n))