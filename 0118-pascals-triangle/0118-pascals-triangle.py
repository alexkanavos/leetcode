class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            elif i == 1:
                pascal.append([1,1])
            else:
                new_list = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        new_list.append(1)
                    else:
                        new_list.append(pascal[i-1][j-1] + pascal[i-1][j])
                pascal.append(new_list)
        return pascal
                