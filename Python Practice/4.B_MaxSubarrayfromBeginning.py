'''
Given an integer array nums, find the contiguous subarray
that includes the first element of the array (containing
at least one number) which has the largest sum and return
its sum.
'''

def maximum_subarray_incl_first_element(array):
  tot = temp = 0
  for num in array:
    temp += num
    if temp > tot:
      tot = temp
  return tot