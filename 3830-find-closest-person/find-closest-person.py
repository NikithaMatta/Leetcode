class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx  == dy:
            return 0
        elif dx < dy:
            return 1
        return 2
        