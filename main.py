class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log_n = math.log(n, 4)
        return log_n == int(log_n)
        
