def bubble_sort_swaps(nums):
  count = 0
  for y in range(len(nums)-1,0,-1):
    finished = True
    for x in range(y):
      if nums[x] > nums[x+1]:
        temp = nums[x]
        nums[x] = nums[x+1]
        nums[x+1] = temp
        count += 1
        finished = False
    if finished == True:
      break
  return count
test = [6, 2, 4, 3]
print(bubble_sort_swaps(test))