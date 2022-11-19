class Solution:
    
    def __init__(self):
        self.mem = {0:1, 1:1}
        
    def climbStairs(self, n: int) -> int:
        
        if n in self.mem:
            return self.mem[n]

        self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.mem[n]
        