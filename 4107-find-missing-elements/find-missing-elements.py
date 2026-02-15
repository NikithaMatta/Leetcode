class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        num_set = set(nums)
        res = []
        for i in range(small, large):
            if i+1 not in num_set:
                res.append(i+1)
        return res
        