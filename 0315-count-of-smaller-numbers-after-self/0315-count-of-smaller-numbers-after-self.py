class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n

        # Store value with original index
        arr = []
        for i in range(n):
            arr.append((nums[i], i))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = 0
            j = 0

            # Count how many elements from right are smaller
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    ans[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                ans[left[i][1]] += j
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)
        return ans