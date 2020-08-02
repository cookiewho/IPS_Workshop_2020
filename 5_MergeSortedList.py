def merge_sorted_list(nums1, nums2):
  y = 0
  for x in range(len(nums1)):
    if nums1[x] >= nums2[y] or nums1[x] == 0:
      nums1.pop()
      nums1.insert(x, nums2[y])
      y+=1
  return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge_sorted_list(nums1,nums2))