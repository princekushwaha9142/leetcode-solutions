class Solution(object):
    def findKthPositive(self, arr, k):
        num = 1
        i = 0
        missing_count = 0

        while missing_count < k:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return num
            num += 1

        return num