### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # implement this method
  ###EVERYTHING BELOW IS MINE, REST WAS PROVIDED###
  def kth_from_the_end(self, k):
    curr = self.head
    while curr != self.tail:
      temp = curr
      for x in range(k):
        temp = temp.next
      if temp.next == None:
        return curr.data
      curr = curr.next
    if curr.next == None:
        return curr.data
    return
  
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])
print(ll.kth_from_the_end(0))