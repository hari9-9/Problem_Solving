class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        for ch in p:
            target[ch] = target.get(ch, 0) + 1

        window = {}
        j = 0  # Left pointer
        ans = []
        p_len = len(p)

        for i in range(len(s)):  # Right pointer
            # Add current character to window
            window[s[i]] = window.get(s[i], 0) + 1

            # If window size exceeds p, remove the leftmost character
            if i - j + 1 > p_len:
                window[s[j]] -= 1
                if window[s[j]] == 0:
                    del window[s[j]]
                j += 1  # Move left pointer

            # If window matches target, add the starting index
            if window == target:
                ans.append(j)

        return ans
