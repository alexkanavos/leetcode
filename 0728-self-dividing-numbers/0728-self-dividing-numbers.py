class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans: list[int] = []
        for num in range(left, right + 1):
            if '0' in str(num):
                continue
            temp: list[int] = [int(i) for i in str(num)]
            success: bool = True
            for d in temp:
                if num % d != 0:
                    success = False
                    break
            if success:
                ans.append(num)
        return ans
                
                
            
            