import bisect

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = self.binarySearch(nums, 0)
        pov = len(nums) - self.binarySearch(nums, 1)
        return max(neg, pov)

    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        result = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                result = mid
                high = mid - 1
        return result