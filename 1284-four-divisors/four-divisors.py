class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divs = set()
            i = 1

            while i*i <= n:
                if n%i == 0:
                    divs.add(i)
                    divs.add(n//i)
                if len(divs) > 4:
                    break
                i += 1
            
            if len(divs) == 4:
                total += sum(divs)
        return total
        