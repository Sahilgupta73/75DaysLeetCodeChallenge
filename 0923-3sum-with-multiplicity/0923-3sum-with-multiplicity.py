class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7

        freq = [0] * 101

        for num in arr:
            freq[num] += 1

        ans = 0

        for x in range(101):
            for y in range(x, 101):
                z = target - x - y

                if z < y or z > 100:
                    continue

                if x == y == z:
                    ans += freq[x] * (freq[x] - 1) * (freq[x] - 2) // 6

                elif x == y != z:
                    ans += freq[x] * (freq[x] - 1) // 2 * freq[z]

                elif x < y == z:
                    ans += freq[x] * freq[y] * (freq[y] - 1) // 2

                else:
                    ans += freq[x] * freq[y] * freq[z]

                ans %= MOD

        return ans