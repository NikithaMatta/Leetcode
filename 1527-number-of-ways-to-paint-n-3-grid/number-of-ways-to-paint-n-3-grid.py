class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        case1 = 6
        case2 = 6

        for _ in range(1, n):
            new_case1 = (3*case1+ 2*case2) % MOD
            new_case2 = (2*case1+ 2*case2) % MOD
            case1, case2 = new_case1, new_case2

        return (case1+case2) % MOD
            

        