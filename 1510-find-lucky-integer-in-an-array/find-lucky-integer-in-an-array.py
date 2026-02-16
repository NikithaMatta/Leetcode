from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        luck = -1
        for num, freq in count.items():
            if num == freq:
                luck = max(luck, num)
        return luck

        