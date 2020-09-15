def binarySearch(nums, find_num, start, stop):
  if start > stop:
    return -1
  else:
    mid = start+((stop-start)//2) 
    print(mid)
    if nums[mid] == find_num:
      return mid
    elif find_num < nums[mid]:
      return binarySearch(nums, find_num, start, mid-1)
    else:
      return binarySearch(nums, find_num, mid+1, stop)
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binarySearch(nums, 1, 0, len(nums)-1))