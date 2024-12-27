class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        print(s)

        # Remove empty strings using a loop
        result = []
        for word in s:
            if word:
                result.append(word)

        result.reverse()
        return ' '.join(result)

        
