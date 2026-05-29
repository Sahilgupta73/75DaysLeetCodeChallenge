class Solution {
public:
    int nextIndex(vector<int>& nums, int i) {
        int n = nums.size();

        int next = (i + nums[i]) % n;

        if (next < 0) {
            next += n;
        }

        return next;
    }

    bool circularArrayLoop(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue;

            int slow = i;
            int fast = i;

            while (true) {
                int nextSlow = nextIndex(nums, slow);

                int nextFast = nextIndex(nums, fast);
                int nextNextFast = nextIndex(nums, nextFast);

                // direction check
                if (nums[slow] * nums[nextSlow] < 0) break;
                if (nums[fast] * nums[nextFast] < 0) break;
                if (nums[nextFast] * nums[nextNextFast] < 0) break;

                slow = nextSlow;
                fast = nextNextFast;

                if (slow == fast) {
                    // cycle of length 1 is not allowed
                    if (slow == nextIndex(nums, slow)) {
                        break;
                    }

                    return true;
                }
            }

            // mark visited path as 0
            int index = i;
            int direction = nums[i];

            while (nums[index] * direction > 0) {
                int next = nextIndex(nums, index);
                nums[index] = 0;
                index = next;
            }
        }

        return false;
    }
};