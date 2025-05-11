from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ct = Counter(nums)
        for c in ct:
            if ct[c] != 1:
                return True
        return False
