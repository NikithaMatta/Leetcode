class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0
        doubleSum = 0

        for num in nums:
            if num < 10:
                singleSum += num
            else:
                doubleSum += num
        
        if singleSum != doubleSum:
            return True
        return False