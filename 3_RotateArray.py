def rotate_array(input_array, k):
  if len(input_array) == 0 or len(input_array) == 1:
    return
  else:
    temp = input_array[len(input_array)-k:len(input_array)]
    for z in range(k):
      input_array.pop()
    input_array[0:0] = temp
    print(input_array)
    return
    
  '''
    for z in range(k):
    temp = input_array[len(input_array)-1]
    for x in range(len(input_array)-1,0,-1):
      input_array[x] = input_array[x-1]
    input_array[0] = temp
  return
  print(rotate_array([-1,-100,3,99],2))
  '''