class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral character to its integer value
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            # If the current value is less than the next value, subtract it
            if i + 1 < length and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            # Otherwise, add it to the running total
            else:
                total += roman_map[s[i]]
                
        return total
