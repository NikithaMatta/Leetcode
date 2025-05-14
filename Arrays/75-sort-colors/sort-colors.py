class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = defaultdict(int)
        for num in nums:
            bucket[num] += 1
        
        index = 0
        for color in [0, 1, 2]:
            for _ in range(bucket[color]):
                nums[index] = color
                index += 1