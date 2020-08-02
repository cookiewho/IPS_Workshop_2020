def atoi(a):
  a = a.strip()
  if len(a) == 0:
    return 0
  number=""
  neg = False
  sign_count = 0
  start = 0
  if ord(a[0]) == 45:
    neg = True
    start+=1
  elif ord(a[0]) == 43:
    start+=1
  for x in range(start, len(a)):
    if ord(a[x]) > 57 or ord(a[x])<48:
      if len(number) == 0:
        return 0
      else:
        break
    else:
      number += a[x]
  if len(number) == 0:
    return 0
  if int(number) >= (2147483648):
    if neg:
      return -(2147483648)
    else:
      return (2147483647)
  else:
    fin = int(number)
  if(neg):
    return -fin
  else:
    return fin