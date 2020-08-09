### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
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
  
  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
  def to_array(self):
    array = []
    curr = self.head
    while curr != None:
      array.append(curr.data)
      curr = curr.next
    return array
  
  # implement this method
  ###RECURSIVE METHOD HIT MAX RECURSIVE DEPTH WITH LARGER NUMBERS###
  ###CODE BELOW IS MINE, REST WAS PROVIDED
  # def recur(self, Node):
  #   if Node == None or Node.next == None:
  #     self.tail = self.head
  #     self.head = Node
  #     return
  #   else:
  #     ll.recur(Node.next)
  #     curr = Node.next
  #     curr.next = Node
  #     Node.next = None
    
  def reverse(self):
    #ll.recur(self.head)
    curr = self.head.next
    prev = self.head
    nex = curr.next
    prev.next = None
    while nex != self.tail:
      curr.next = prev
      prev = curr
      curr = nex
      nex = nex.next
    curr.next = prev
    nex.next = curr
    temp = self.tail
    self.tail = self.head
    self.head = temp
    
  
ll = LinkedList()
# ll.extend(list(range(0,100)))
ll.extend(list(range(0,10000)))
ll.reverse()
print(ll.to_array())