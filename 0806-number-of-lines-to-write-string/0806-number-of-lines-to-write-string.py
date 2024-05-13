class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_line_width: int = 0
        num_of_lines: int = 1
        i: int = 0
        letters: list[chr] = list('abcdefghijklmnopqrstuvwxyz')
        while i < len(s):
            position: int = letters.index(s[i])
            if total_line_width + widths[position] <= 100:
                total_line_width += widths[position]
            else:
                num_of_lines += 1
                total_line_width = 0
                i -= 1
            i += 1
        return [num_of_lines, total_line_width]
            