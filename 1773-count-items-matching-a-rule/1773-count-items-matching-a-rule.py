class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        num: int = 0
        if ruleKey == 'type':
            for i in range(len(items)):
                if items[i][0] == ruleValue:
                    num += 1
        elif ruleKey == 'color':
            for i in range(len(items)):
                if items[i][1] == ruleValue:
                    num += 1
        elif ruleKey == 'name':
            for i in range(len(items)):
                if items[i][2] == ruleValue:
                    num += 1
        return num