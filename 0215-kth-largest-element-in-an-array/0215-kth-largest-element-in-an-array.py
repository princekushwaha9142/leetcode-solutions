import random

class Solution(object):
    def findKthLargest(self, nums, k):
        target = len(nums) - k  # 0-indexed position jo chahiye sorted order mein

        def quick_select(left, right):
            pivot = nums[random.randint(left, right)]
            lt, gt = left, right
            i = left
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            # ab nums[lt..gt] sab == pivot hain
            if target < lt:
                return quick_select(left, lt - 1)
            elif target > gt:
                return quick_select(gt + 1, right)
            else:
                return pivot

        return quick_select(0, len(nums) - 1)