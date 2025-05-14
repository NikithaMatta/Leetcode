from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        lt = []
        for num in nums:
            if ct[num] > (len(nums)//3) and num not in lt:
                lt.append(num)
        return lt