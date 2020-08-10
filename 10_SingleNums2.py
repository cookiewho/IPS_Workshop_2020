###nums appear three times###
def single_number_three(nums):
  ans = 0
  twos = 0
  for x in range(len(nums)):
    ans = (ans ^nums[x]) & ~twos
    twos = (twos ^ nums[x]) & ~ans
  return ans
arr = [2, 2, 3, 2]
print(single_number_three(arr))

###nums appear two times###
def single_number_two(nums):
  ans = 0
  for x in range(len(nums)):
    ans ^= nums[x]
  return ans
arr = [2, 1, 3, 1, 2]
print(single_number_two(arr))