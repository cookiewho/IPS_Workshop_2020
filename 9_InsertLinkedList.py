### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
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
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  ### CODE BELOW IS MINE, REST WAS PROVIDED###
  def insert(self, data, index):
    if index == 0:
      new_head = LinkedNode(data)
      new_head.next = self.head
      self.head = new_head
      return
    ind = 1
    curr = self.head
    while curr != self.tail:
      curr = curr.next
      ind +=1
      if ind == index:
        new_node = LinkedNode(data)
        new_node.next = curr.next
        curr.next = new_node
        if curr == self.tail:
          self.tail = new_node
        return
    return
    
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])

ll.insert(4,2)
