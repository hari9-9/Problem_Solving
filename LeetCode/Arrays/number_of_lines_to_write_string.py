class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        num_lines = 1
        curr_width = 0
        for ch in s:
            if curr_width + (widths[ord(ch) - ord('a')]) <=100:
                curr_width += widths[ord(ch) - ord('a')]
            else:
                num_lines+=1
                curr_width = widths[ord(ch) - ord('a')]
        return num_lines , curr_width
