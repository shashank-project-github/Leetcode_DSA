class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        while slow:
            next_node = slow.next
            slow.next = previous 
            previous = slow
            slow = next_node

        first = head
        second = previous

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True