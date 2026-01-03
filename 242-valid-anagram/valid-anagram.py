class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ct = Counter(s)
        t_ct = Counter(t)
        if s_ct == t_ct:
            return True
        return False