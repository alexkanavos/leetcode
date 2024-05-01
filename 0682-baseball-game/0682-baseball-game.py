class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores: list[int] = []
        for el in operations:
            if el == 'C':
                scores.pop(-1)
            elif el == 'D':
                scores.append(2 * scores[-1])
            elif el == '+':
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(el))
        return sum(scores)