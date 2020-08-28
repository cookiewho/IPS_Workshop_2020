'''
List of Depths: Given a binary tree, design an algorithm which creates a
linked list of all the nodes at each depth (e.g., if you have a tree with
depth 0, you'll have 0 linked lists).
'''
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None
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

tree = Tree()
tree.add(Node(5))
tree.add(Node(3))
tree.add(Node(1))
tree.add(Node(4))
tree.add(Node(7))
tree.add(Node(6))
tree.add(Node(8))
### ACTUAL PROBLEM CODE BELOW ###
class LL_Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class LinkedList():
  def __init__(self):
    self.root = None
  
  def add(self,num):
    if self.root == None:
      self.root = LL_Node(num)
    else:
      curr = self.root
      while curr.nextval !=None:
        curr =  curr.nextval
      curr.nextval = LL_Node(num)
    return
  
  def show(self):
    if self.root == None:
      print("oops")
      return
    else:
      s = ""
      curr = self.root
      while curr.nextval !=None:
        s += str(curr.dataval) + ", " 
        curr =  curr.nextval
      s += str(curr.dataval) 
    return s

def levelOrderList(root):
  ans = []
  def dfs(curr, count):
    if curr == None:
      return
    else:
      if len(ans)< count+1:
        temp = LinkedList()
        temp.add(curr.data)
        ans.append(temp)
      else:
        ans[count].add(curr.data)
      dfs(curr.left, count+1)
      dfs(curr.right,count+1)
      
  dfs(root,0)

  final = "["
  for x in ans:
    final += "[" + x.show() + "], "
  return final[0:-2] +"]"
  # return ans# once we modify ans = [linked Lists]
print(levelOrderList(tree.root))

'''
THOUGHT THAT IT WAS A LINKED LIST OF LISTS(hence the code below), BUT WAS NOT THE CASE
      # ans[0].append(curr)
      temp = count
      currLL = ans.root
      while(temp != 0):
        if currLL == None:

        currLL = currLL.nextval
        temp-=1
      currLL.dataval.append(curr)
'''
'''
FIRST THOUGHT OF BFS, BUT GOT CONFUSED AND SWITCHED TO DFS B/C IT MADE MORE SENSE IN MY BRAIN
curr = root
queue = [[root,0]]
count = 0
while len(queue) > 0:
  curr = queue.pop(0)
  count+=1
  if curr.left != None:
    queue.append(curr.left)
  if curr.righ != None:
    queue.append(curr.right)
'''