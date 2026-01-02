class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                num = nums[i]
                break
            seen.add(nums[i])
        return num