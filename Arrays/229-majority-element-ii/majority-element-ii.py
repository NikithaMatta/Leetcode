from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        lt = set()
        for num in nums:
            if ct[num] > (len(nums)/3):
                lt.add(num)
        return list(lt)