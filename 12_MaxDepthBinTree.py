# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    def recurr(curr, maxN, count):
      if curr != None:
        print(curr.val, maxN, count)
        maxN = recurr(curr.left, maxN, count+1)
        maxN = recurr(curr.right, maxN, count+1)
        return maxN
      else:
        if count >= maxN:
          return count
        return maxN
    return recurr(root, 0, 0)
        