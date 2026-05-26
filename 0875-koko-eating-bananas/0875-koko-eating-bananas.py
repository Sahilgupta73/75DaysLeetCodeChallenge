class Solution:
    def minEatingSpeed(self, piles, h):
        # left is the minimum possible eating speed
        # Koko can eat at least 1 banana per hour
        left = 1

        # right is the maximum possible eating speed
        # Eating faster than the largest pile is not needed
        right = max(piles)

        # Binary search will run until left and right become equal
        while left < right:

            # mid is the current eating speed we are testing
            mid = (left + right) // 2

            # hours will store total hours needed at speed mid
            hours = 0

            # Check every pile one by one
            for pile in piles:

                # Calculate hours needed for this pile
                # This is same as ceil(pile / mid)
                # Example: pile = 11, mid = 4
                # (11 + 4 - 1) // 4 = 14 // 4 = 3 hours
                hours += (pile + mid - 1) // mid

            # If total hours are less than or equal to h,
            # it means speed mid is enough
            if hours <= h:

                # But we need minimum speed,
                # so try to find smaller speed on the left side
                right = mid

            # If total hours are greater than h,
            # it means speed mid is too slow
            else:

                # So we increase the speed
                left = mid + 1

        # When loop ends, left is the minimum valid eating speed
        return left