# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		r = 0
		ret = ListNode()
		while l1 or l2 or r:
			print(l1)
			print(l2)
			l1v = l1.val if l1 else 0
			l2v = l2.val if l2 else 0
			s, r= divmod(l1v+l2v+ (r*10), 10)
			ret.val = s
			ret.next = ret
			l1 = l1.next if l1 else False
			l2=l2.next if l2 else False
			
		return ret

print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))