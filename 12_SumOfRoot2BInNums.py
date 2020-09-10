'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf
path represents a binary number starting with the most significant
bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this
could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by
the path from the root to that leaf.

Return the sum of these numbers.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    tot = 0
    s = []
    def recur(curr, tot):
      s.append(curr.val)
      if curr.left == None and curr.right == None:
        m = 1
        for x in s[::-1]:
          tot += x * m
          m*=2
        s.pop(-1)
        return tot
      else:
        if curr.left != None:
          tot = recur(curr.left, tot)
        if curr.right != None:
          tot = recur(curr.right, tot)
        s.pop(-1)
        return tot
    tot = recur(root, tot)
    return tot