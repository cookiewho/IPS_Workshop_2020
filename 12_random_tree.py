'''
  Randomly
       A
    /      \
   B       C
 /   \      /   \
D  E    F  G
'''
import random
values = []
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None
    
  def traverse(self):
    def recurr(node):
      if node == None:
        return
      else:
        values.append(node.data)
        if node.left != None:
          recurr(node.left)

        if  node.right != None:
          recurr(node.right)
          
    recurr(self.root)

  def add(self,node):
    if not self.root:
      self.root = node
      return
    curr = self.root
    def add_to_tree(self, curr):
      if node.data < curr.data:
        if curr.left == None:
          curr.left = node
          return
        add_to_tree(self, curr.left)
      if node.data > curr.data:
        if curr.right == None:
          curr.right = node
          return
        add_to_tree(self, curr.right)
    add_to_tree(self, curr)

  def traverse2(self):
    curr = self.root
    stack = [curr]
    while len(stack) > 0:
      curr = stack.pop(-1)	
      values.append(curr.data)
      if curr.left != None:
        stack.append(curr.left)
      if curr.right != None:
        stack.append(curr.right)
		
  def rand_order(self):
    def recurr(node):
      if node == None:
        return
      else:
        index = random.randint(0, len(values)-1)
        node.data = values.pop(index)
        if node.left != None:
          recurr(node.left)
        if  node.right != None:
          recurr(node.right)
    recurr(self.root)

  def in_order_traversal(self):
    nodes = []
    def dfs(node):
      if node:
        dfs(node.left)
        nodes.append(node.data)
        dfs(node.right)
    dfs(self.root)
    return nodes
# Values = [A, B, D, E, C, F, G]

tree = Tree()
tree.add(Node('C'))
tree.add(Node('A'))
tree.add(Node('B'))
tree.add(Node('F'))
tree.add(Node('G'))
tree.add(Node('H'))
tree.add(Node('I'))
tree.add(Node('K'))
tree.traverse()
print (values)
print(tree.in_order_traversal())
print (values)
tree.rand_order()
print (values)
print(tree.in_order_traversal())
