class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

    ## INSTEAD, non binary
    self.children = []

    self.parent = None

class Tree:
  def __init__(self):
    self.root = None

  def in_order_traversal(self):

    def dfs(node):
      if node:

        dfs(node.left)
        print(node.data)
        dfs(node.right)

    dfs(self.root)

  def level_order_traversal(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      if current_node.left:
        queue.append(current_node.left)
      print(current_node.data)
      if current_node.right:
        queue.append(current_node.right)

  def add(self,node):
    if not self.root:
      self.root = node
      return 

    def insert(root, node):
      if root.data > node.data:
        if root.left is None:
          root.left = node
        else:
          insert(root.left, node)
      else:

        if root.right is None:
          root.right = node
        else:
          insert(root.right, node)
    
    insert(self.root, node)

  def height(self):

    def get_height(node):

      if node is None:
        return 0
      else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if left_height > right_height:
          return left_height +1
        else:
          return right_height +1
    return get_height(self.root)
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  '''
  class Solution:
  ### EVERYTHING BELOW IS MINE ###
  ### LEET CODE APPROVED ###
      def balanceBST(self, root: TreeNode) -> TreeNode:
          order = []
          def dfs_list(node):
              if node:
                  dfs_list(node.left)
                  order.append(node.val)
                  dfs_list(node.right)
          dfs_list(root)
          def recur(start, end):
  
              if start>end:
                  return None

              mid = (start+end)//2
              node= TreeNode(order[mid])

              node.left = recur(start, mid-1)
              node.right = recur(mid+1, end)
              return node
          root = recur(0, len(order)-1)
          return root
          '''
  def balance(self):
    # write a function to reduce the height of this tree as much as possible
    order = []
    print("height = " + str(self.height()))
    def dfs_list(node):
      if node:
        dfs_list(node.left)
        order.append(node.data)
        dfs_list(node.right)
    dfs_list(self.root)
    print(order)
    ### RECURSIVE APPROACH WITH SOME HELP  ###
    def recur(start, end):
      if start>end:
          return None

      mid = (start+end)//2
      node= Node(order[mid])

      node.left = recur(start, mid-1)
      node.right = recur(mid+1, end)
      return node
    self.root = recur(0, len(order)-1)
    return self.root
    ''' 
    ### ITERATIVE APPROACH BY MYSELF  ###
    mid = (len(order)-1)//2
    self.root= Node(order[mid])
    x = mid-1
    x = mid-1
    while x >= 0:
      if x-2 < 0:
        self.add(Node(order[x]))
        self.add(Node(order[x-1]))
        x-=2
      else:
        self.add(Node(order[x-1]))
        self.add(Node(order[x-2]))
        self.add(Node(order[x]))
        x-=3
    y = mid+1
    while y <= len(order)-1:
      if y+2  > len(order):
        self.add(Node(order[y]))
        self.add(Node(order[y+1]))
        y+=2
      else:
        self.add(Node(order[y+1]))
        self.add(Node(order[y+2]))
        self.add(Node(order[y]))
        y+=3
    print(self.height())
  '''
  
  
  
tree = Tree()

tree.add(Node(6))
tree.add(Node(27))
tree.add(Node(15))
tree.add(Node(10))
tree.add(Node(13))
tree.add(Node(8))
print(tree.level_order_traversal())
print()
print(tree.balance())
print()
print(tree.level_order_traversal())