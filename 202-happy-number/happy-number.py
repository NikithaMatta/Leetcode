class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            res = 0
            while n > 0:
                res += (n%10) ** 2
                n //= 10
            n = res
        return True if n == 1 else False
        