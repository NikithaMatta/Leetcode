class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val = {}
        for i in arr:
            if i not in val:
                val[i] = 1
            else:
                val[i] += 1
        num = set(val.values())
        return len(num) == len(val)

        