class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        if 'IV' in s:
            num += 4
            s = s.replace('IV','')
        if 'IX' in s:
            num += 9
            s = s.replace('IX','')
        if 'XL' in s:
            num += 40
            s = s.replace('XL','')
        if 'XC' in s:
            num += 90
            s = s.replace('XC','')
        if 'CD' in s:
            num += 400
            s = s.replace('CD','')
        if 'CM' in s:
            num += 900
            s = s.replace('CM','')

        for c in s:
            if c == 'M':
                num += 1000
            if c == 'D':
                num += 500
            if c == 'C':
                num += 100
            if c == 'L':
                num += 50
            if c == 'X':
                num += 10
            if c == 'V':
                num += 5
            if c == 'I':
                num += 1
        return num