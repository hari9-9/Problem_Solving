class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if not s :
            return ""
        if not part:
            return s
        stack = []
        part = list(part)
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part) and stack[-len(part):] == part:
                for i in range(len(part)):
                    stack.pop()
        return "".join(stack)
