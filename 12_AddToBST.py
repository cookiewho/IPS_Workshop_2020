class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None

  def print_bfs(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      print(current_node.data)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

  def in_order_traversal(self):
    nodes = []
    def dfs(node):
      if node:
        
        dfs(node.left)
        nodes.append(node.data)
        dfs(node.right)

        
    dfs(self.root)
    return nodes
### ALL CODE BELOW IS MINE, REST WAS PROVIDED ###
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
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = Tree()
tree.add(Node(55))
tree.add(Node(20))
tree.add(Node(30))
tree.add(Node(100))
tree.add(Node(15))
tree.add(Node(200))
tree.add(Node(60))
print(tree.in_order_traversal())
