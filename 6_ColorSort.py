def color_sort(nums):
    # LEETCODE APPROVED
    last_zero = 0
    x = 0
    untouched = len(nums)
    while x < untouched:
    #for x in range(len(nums)):
        if nums[x] == 0:
            nums.insert(0, nums.pop(x))
            last_zero +=1
        elif nums[x] == 2:
            nums.insert(len(nums), nums.pop(x))
            untouched -=1
            x-=1
        x+=1
    return nums
test = [1,1,0,0,2,1,1,1,0,2,0]
print(color_sort(test))