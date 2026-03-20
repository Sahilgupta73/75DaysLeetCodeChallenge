class Solution(object):
    def isPalindrome(self, s):
        # Step 1 & 2: clean the string
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        
        # Step 3: check palindrome
        return cleaned == cleaned[::-1]