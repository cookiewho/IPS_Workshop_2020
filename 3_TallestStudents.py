def height_rows(student_heights):
  arr = [[student_heights[0]]]
  row  = 0
  for x in student_heights:
    if arr[row][-1] >= x:
      arr[row].append(x)
    else:
      arr.append([x])
  return (len(arr))
test1 = [5, 4, 8, 1]          #2
test2 = [8, 6, 9,12, 14, 5]   #4
print(height_rows(test1))
print(height_rows(test2))
