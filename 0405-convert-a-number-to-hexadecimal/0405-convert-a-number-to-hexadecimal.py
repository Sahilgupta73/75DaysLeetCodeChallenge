class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        num &= 0xFFFFFFFF
        res = []

        while num > 0:
            res.append(hex_chars[num & 0xF])
            num >>= 4

        return "".join(reversed(res))