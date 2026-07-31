# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        # Convert l1 to array
        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        # Convert l2 to array
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        ans = []
        carry = 0
        i = j = 0

        # Add the two arrays
        while i < len(arr1) or j < len(arr2) or carry:
            x = arr1[i] if i < len(arr1) else 0
            y = arr2[j] if j < len(arr2) else 0

            total = x + y + carry
            ans.append(total % 10)
            carry = total // 10

            i += 1
            j += 1

        # Convert answer array back to linked list
        dummy = ListNode(0)
        curr = dummy

        for num in ans:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next