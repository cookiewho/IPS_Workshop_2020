def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
  print (k)
  print(arr)
  return k
def is_sorted(arr):
  for x in range(len(arr)-1):
    if arr[x] > arr[x+1]:
      return False
  return True
def pancake_sort(nums):
  k_vals = []
  unsorted = len(nums)
  while(unsorted > 0):
    max_ind = 0
    for x in range(unsorted):
      if nums[x] > nums[max_ind]:
        max_ind = x
    if max_ind != 0:
      k_vals.append(flip(nums, max_ind+1))
    k_vals.append(flip(nums, unsorted))
    unsorted-=1
    max_ind =0
    if is_sorted(nums):
      return k_vals
  return k_vals
test = [5, 2, 3, 4, 1]
print(pancake_sort(test))