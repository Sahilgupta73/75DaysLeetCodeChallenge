class Solution(object):
    def vowelStrings(self, words, left, right):
        vowel = "aeiou"
        count = 0
        for i in range(left,right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                count = count+1
        
        return count