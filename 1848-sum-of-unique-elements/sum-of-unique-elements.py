from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        sumi = 0
        for num, freq in count.items():
            if freq == 1:
                sumi += num
        return sumi
        