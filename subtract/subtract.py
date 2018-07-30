# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def subtract(self, A):
		if A == None:
			# list is empty
			return A

		# get length of list
		L = 1
		cursor = A
		while (cursor.next != None):
			L += 1
			cursor = cursor.next

		# take the first floor(L/2) elements and put them in a new list (B) in reverse order
		temp = None
		for i in range(L//2):
			B = A
			A = A.next
			B.next = temp
			temp = B

		cursorA = A
		cursorB = B

		# if list has odd length, skip middle element
		if L % 2 == 1:
			cursorA = cursorA.next

		# cursorA and cursorB now have equal length

		# modify values of nodes
		while (cursorA != None):
			cursorB.val = cursorA.val - cursorB.val
			cursorA = cursorA.next
			cursorB = cursorB.next

		# merge lists back together by taking front of B and moving to front of A
		while (B != None):
			temp = A
			A = B
			B = B.next
			A.next = temp

		return A
