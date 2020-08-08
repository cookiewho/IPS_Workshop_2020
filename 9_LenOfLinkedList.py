### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than length()
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
  # return the length of the linked list, an integer value
  #MY CODE IS BELOW THIS, REST WAS PROVIDED
  def length(self):
    if self.empty():
      return 0
    else:
      length = 1
      curr = self.head
      while curr != self.tail:
        length += 1
        curr = curr.next
      return length
    
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5])

print (ll.length())