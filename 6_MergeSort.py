def merge_sort(nums):
    if(len(nums) > 1):
        mid = int(len(nums)//2)
        left = merge_sort(nums[0:mid])
        right = merge_sort(nums[mid:])
        new_nums = []
        while(len(left) > 0 and len(right) >0):
            if left[0] < right[0]:
                new_nums.append(left.pop(0))
            else:
                new_nums.append(right.pop(0))
            new_nums.extend(left)
            new_nums.extend(right)
    else:
        return nums
    return new_nums

print(merge_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))