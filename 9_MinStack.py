class StackNode:
  def __init__(self, data):
    self.data = data
    self.previous = None
    
class MinStack(object):

  def __init__(self):
    self.topN = None
    return

  def push(self, x):
    new_topN = StackNode(x)
    if self.topN == None:
      self.topN = new_topN
    else:
      new_topN.previous = self.topN
      self.topN = new_topN
    return
      

  def pop(self):
    if self.topN == None:
      return
    else:
      temp = self.topN
      self.topN = self.topN.previous
      temp.previous = None
      del temp
    return

  def top(self):
    return self.topN.data
      

  def getMin(self):
    if self.topN == None:
      return
    else:
      curr = self.topN
      min_num = curr.data
      while curr.previous != None:
        curr = curr.previous
        if curr.data < min_num:
          min_num = curr.data
      return min_num
      
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.topN()
# param_4 = obj.getMin()
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin())
minStack.pop();
print(minStack.top())    
print(minStack.getMin())