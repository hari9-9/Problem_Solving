class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(left: int, right: int) -> None:
            # Base case: stop if pointers have crossed
            if left >= right:
                return

            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]

            # Recursive call with the next positions inward
            rev(left + 1, right - 1)

        # Initialize the recursion with the full array bounds
        rev(0, len(s) - 1)
