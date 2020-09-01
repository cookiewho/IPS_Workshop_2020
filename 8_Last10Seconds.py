'''
Time      Number    Have we seen this number in the last 10 seconds?
  1         5         False
  3         1         False
  7         6         False
  8         5         True
  18        1         False
'''
'''
### Seudo_Code ###
Queue = []
If queue is empty:
Append
Get our pair
Compare time to last time in queue, check if diff greater than 10
If yes, pop, check new last
If no, go through queue and check if duplicate
'''
'''
### method signature for Binary Search ###
Def binarySearch(list_of_items, number):
“””
Returns the index of the number we are looking for
Returns False if number not found
“””
'''

class Dictionary:
	def __init__(self):
		Self.dict = {}

def isDuplicated(self, time, num):
		ind = binarySearch(self.dict, time)
		# Delete items that are less than this index
		if ind:
			if num in self.dict:
				self.dict[num] = time
				return True
		self.dict[num] = time
		return False
### Solution using a Queue, O(1) time and space complexity ###
class Queue:
	def __init__(self):
		Self.queue = [[8,5], [18,1]]

def isDuplicated(self, time, num):
  while len(self.queue) !=0 and (time - self.queue[0][0])>10:
    self.queue.pop(0)
  for x in self.queue:
    if x[1] == num:
      self.queue.append([time, num])
      return True
  self.queue.append([time, num])
  return False		

