class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        f0 = 0
        f1 = 1
        for i in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2
        