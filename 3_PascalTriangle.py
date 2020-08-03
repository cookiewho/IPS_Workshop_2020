def pascal_triangle(numRows):
  triangle = []
  for x in range(1,numRows+1):
    temp = []
    if x >= 2:
      temp.append(1)
      for y in range(len(triangle[-1])-1):
        temp.append(triangle[-1][y]+triangle[-1][y+1])
    temp.extend([1])
    triangle.append(temp)
  print("[")
  for x in triangle:
    if x == triangle[-1]:
      print("     "+str(x))
    else:
      print("     "+str(x) +",")
  print("]")
  return triangle

pascal_triangle(5)