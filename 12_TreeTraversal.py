class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class Tree:
  def __init__(self):
    self.root = None
    
    
  def level_order_traversal(self):
    traversal_order = []
    if self.root == None:
      return
    else:
      queue = [self.root]
      while len(queue) >0:
        curr = queue.pop(0)
        traversal_order.append(curr.data)
        if curr.left != None:
          queue.append(curr.left)
        if curr.right != None:
          queue.append(curr.right)
    # return the tree as a list in a level-order sequence
    return traversal_order
    
    
    
  def pre_order_traversal(self):
    traversal_order = []
    def dfs(Node):
      if Node != None:
        traversal_order.append(Node.data)
        dfs(Node.left)
        dfs(Node.right)
    dfs(self.root)
    # return the tree as a list in a pre-order sequence (dfs)
    return traversal_order
    
  def in_order_traversal(self):
    traversal_order = []
    def dfs(Node):
      if Node != None:
        dfs(Node.left)
        traversal_order.append(Node.data)
        dfs(Node.right)
    dfs(self.root)
    # return the tree as a list in-order (dfs)
    return traversal_order
    
  def post_order_traversal(self):
    traversal_order = []
    def dfs(Node):
      if Node != None:
        dfs(Node.left)
        dfs(Node.right)
        traversal_order.append(Node.data)
    dfs(self.root)
    # return the tree as a list in a post-order sequence (dfs)
    
    return traversal_order

tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

print(tree.level_order_traversal())
print(tree.pre_order_traversal())
print(tree.in_order_traversal())
print(tree.post_order_traversal())