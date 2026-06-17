class Solution:
    def reverseList(self, head):
        reversed_list = None
        current = head

        while current:
            next_node = current.next

            current.next = reversed_list
            reversed_list = current

            current = next_node

        return reversed_list