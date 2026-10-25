class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        def count_pairs(bound):
            left = 0
            right = len(nums) - 1
            count = 0
            while left < right:
                if nums[left] + nums[right] <= bound:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
        return count_pairs(upper) - count_pairs(lower - 1)