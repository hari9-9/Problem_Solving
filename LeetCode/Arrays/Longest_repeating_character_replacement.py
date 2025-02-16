class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        char = [0] * 26  # Frequency array for 'A' to 'Z'
        max_freq = 0  # Track max frequency of any character in window
        left = 0  # Left pointer
        res = 0  # Store max length

        for right in range(len(s)):
            char[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, char[ord(s[right]) - ord('A')])

            # Window size: (right - left + 1), max_freq tells us the dominant character
            while (right - left + 1) - max_freq > k:
                char[ord(s[left]) - ord('A')] -= 1
                left += 1  # Shrink window

            res = max(res, right - left + 1)  # Update max length

        return res
