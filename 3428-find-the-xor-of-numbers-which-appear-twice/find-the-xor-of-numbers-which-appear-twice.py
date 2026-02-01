class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for num in nums:
            if num in seen:
                res ^= num
            else:
                seen.add(num)
        return res