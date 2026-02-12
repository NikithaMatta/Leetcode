class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[n+i])
        return new        