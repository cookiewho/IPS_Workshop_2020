def find_pivot_index(input_list):
  start = 0
  mid = len(input_list)//2
  end = len(input_list)-1
  while(start != mid and end != mid):
    if input_list[mid] < input_list[start]:
      end = mid
      mid = ((end - start)//2) + start
      print ( "start = " +str(start) + ",mid = "+ str(mid) + ",end = " + str(end))
    elif input_list[mid] > input_list[end]:
      start = mid
      mid = ((end - start)//2)+ start
      print ( "start = " +str(start) + ",mid = "+ str(mid) + ",end = " + str(end))
    elif input_list[start] < input_list[mid]:
      end = mid
      mid = ((end - start)//2) + start
    elif input_list[mid] < input_list[end]:
      start = mid
      mid = ((end - start)//2)+ start
  if input_list[start] > input_list[end]:
    return end
  else:
    return start
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
test1=[5137, 5525, 9511, 13269, 16255, 16700, 19870, 23034, 29247, 29934, 34583, 41585, 42598, 44113, 46035, 50147, 50737, 57084, 65916, 76905, 84098, 85912, 92081, 92257, 95449]
print(find_pivot_index(test1))