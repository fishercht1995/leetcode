#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dig = 0
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        l3 = ListNode()
        dumy = l3
        while l1 != None and l2 != None:
            sum_v = l1.val + l2.val + dig
            l3.next = ListNode(val = sum_v % 10)
            l3 = l3.next
            dig = sum_v // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            l3.next = ListNode(val = (l1.val + dig)%10)
            dig = (l1.val + dig) // 10
            l3 = l3.next
            l1 = l1.next
        
        while l2 != None:
            l3.next = ListNode(val = (l2.val + dig)%10)
            dig = (l2.val + dig) // 10
            l3 = l3.next
            l2 = l2.next
        
        if dig > 0:
            l3.next = ListNode(val = dig)
        return dumy.next



# @lc code=end

