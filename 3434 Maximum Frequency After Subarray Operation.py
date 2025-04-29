class Solution(object):
    def maxFrequency(self, nums, k):
        # 1) build the set of possible shifts
        delta_set = set(k - n for n in nums if n != k)
        k_freq   = nums.count(k)
        res      = k_freq

        # 2) for each shift, run a weighted Kadane
        for d in delta_set:
            cur_max, glob_max = 0, 0    # <<< reset these per d
            for n in nums:
                if n + d == k:
                    # this element becomes k → weight = +1
                    cur_max = max(1, cur_max + 1)
                elif n == k:
                    # this element was k but will be shifted away → weight = −1
                    cur_max = max(0, cur_max - 1)
                # else weight = 0 → cur_max stays the same

                glob_max = max(glob_max, cur_max)

            # add back the original k_count for this delta
            res = max(res, k_freq + glob_max)

        return res
