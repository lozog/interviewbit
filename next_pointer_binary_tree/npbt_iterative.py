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
		curr = root

		# keep track of the "first" (leftmost) node in the next level
		leftmostInNextLevel = curr.left

		while curr.left != None:

			curr.left.next = curr.right

			# current level already has its next nodes set
			if curr.next == None:
				# right-most node in a level

				curr = leftmostInNextLevel
				leftmostInNextLevel = curr.left
			else:
				curr.right.next = curr.next.left
				curr = curr.next
