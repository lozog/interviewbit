# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root.left == None:
			# this is a leaf node
			return

		if root.next == None:
			root.left.next = root.right
		else:
			root.left.next = root.right
			root.right.next = root.next.left

		self.connect(root.left)
		self.connect(root.right)
