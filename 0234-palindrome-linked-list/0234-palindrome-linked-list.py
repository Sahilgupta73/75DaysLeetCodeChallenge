# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        temp = head

        # Store linked list values in list
        while temp:
            nums.append(temp.val)
            temp = temp.next

        left = 0
        right = len(nums) - 1

        # Check palindrome
        while left < right:
            if nums[left] != nums[right]:
                return False

            left += 1
            right -= 1

        return True
        