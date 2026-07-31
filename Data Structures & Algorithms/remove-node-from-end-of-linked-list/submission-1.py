# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head

        # Store all nodes in an array
        while curr:
            arr.append(curr)
            curr = curr.next

        remove = len(arr) - n

        # If removing the head
        if remove == 0:
            return head.next

        # Skip the node to be removed
        arr[remove - 1].next = arr[remove].next

        return head