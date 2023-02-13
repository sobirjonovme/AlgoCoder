# # """
# # https://leetcode.com/problems/add-two-numbers/
# # """


# # # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         temp = l1.val + l2.val
#         result = ListNode(temp%10)
#         next_node = result
#         carry = temp // 10

#         while l1.next is not None and l2.next is not None:
#             l1 = l1.next
#             l2 = l2.next
#             temp = l1.val + l2.val + carry
#             next_node.next = ListNode(temp%10)
#             next_node = next_node.next
#             carry = temp//10
        
#         while l1.next is not None:
#             l1 = l1.next
#             temp = l1.val + carry 
#             next_node.next = ListNode(temp%10)
#             next_node = next_node.next
#             carry = temp//10
        
#         while l2.next is not None:
#             l2 = l2.next
#             temp = l2.val + carry 
#             next_node.next = ListNode(temp%10)
#             next_node = next_node.next
#             carry = temp//10
        
#         if carry != 0:
#             next_node.next = ListNode(carry)
        
#         return result
