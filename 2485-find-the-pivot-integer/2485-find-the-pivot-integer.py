class Solution:
    def pivotInteger(self, n: int) -> int:
        x: int = 0
        while True:
            x_sum: int = 0
            n_sum: int = 0
            for a in range(1, x + 1):
                x_sum += a
            for b in range(x, n + 1):
                n_sum += b
            if x_sum > n_sum:
                return -1
            elif x_sum == n_sum:
                return x
            else:
                x += 1
            
                
            