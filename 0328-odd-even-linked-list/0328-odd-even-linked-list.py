# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        oddDummy = ListNode(0)
        evenDummy = ListNode(0)

        odd = oddDummy
        even = evenDummy

        pos = 1
        curr = head

        while curr:
            if pos % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next

            curr = curr.next
            pos += 1

        even.next = None
        odd.next = evenDummy.next

        return oddDummy.next