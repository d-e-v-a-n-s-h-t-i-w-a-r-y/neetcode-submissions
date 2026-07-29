# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        # Store all values in an array
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Write them back in reverse order
        curr = head
        while curr:
            curr.val = arr.pop()
            curr = curr.next

        return head