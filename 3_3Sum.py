class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort() #sort to keep better track of what numbers we have already used(no duplicates)
    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x-1]: #make sure that we  go over any items that would make our set a duplicate sets
            continue
        goal = nums[x] *-1  #if we get y + z == -x, then we have a solution set
        start = x+1         #keep track of y
        end = len(nums)-1   #keep track of z
        while start < end:
            if nums[start] + nums[end] == goal: # y+z = -x, we have a solution set
                ans.append([nums[x], nums[start], nums[end]])
                start += 1
                while start < end and nums[start] == nums[start-1]: #make sure that we  go over any items that would make our set a duplicate sets
                    start += 1
            elif nums[start] + nums[end] < goal:  # y+z < -x, shorten our range forward to get y+z closer to -x
                start += 1
            else:                                 # shorten our range to the back, to get y + z closer to -x
                end -= 1
    return ans
                    