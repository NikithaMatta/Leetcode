class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        sign = 1
        for i in range(n, 0, -4):
            temp = i
            if i-1 > 0: temp *= i-1
            if i-2 > 0: temp //= i-2
            result += sign * temp
            if i-3 > 0: result += i-3
            sign = -1
        return result
        