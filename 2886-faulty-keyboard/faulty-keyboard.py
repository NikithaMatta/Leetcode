class Solution:
    def finalString(self, s: str) -> str:
        r = ""
        for char in s:
            if char == "i":
                r = r[::-1]
            else:
                r += char
        return r
        
        