
def partition(arr, start, end):
  x = start-1
  pivot = arr[end]
  for y in range(start, end):
    if arr[y] < pivot:
      x+=1
      if x!=y:
        arr[x],arr[y] = arr[y],arr[x]
  arr[x+1], arr[end] = arr[end], arr[x+1]
  return(x+1)
def quickSort(arr, start, end):
  if start<end:
    part = partition(arr, start, end)
    quickSort(arr, start, part-1)
    quickSort(arr, part+1, end)
test = [420, 10,30,80,90,40,50,70,100, 55, 20, 47, 69]
print(test)
quickSort(test, 0, len(test)-1)
print(test)