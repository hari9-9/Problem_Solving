# class Solution:
#     def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
#         ans = 0
#         pick =0
#         banned.sort()
#         curr=0
#         for i in range(1,n+1):
#             if curr<len(banned) and i == banned[curr]:
#                 curr+=1
#                 print("skipped")
#                 continue
#             if ans+i >maxSum:
#                 return pick
#             # if ans+i<=maxSum:
#             ans+=i
#             pick+=1
#             print("curr "+str(curr)+" i "+str(i) + " pick "+str(pick) + " ans " + str(ans))
#         return pick
# class Solution:
#     def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
#         ans = 0  # Tracks the sum of chosen numbers
#         pick = 0  # Tracks the count of chosen numbers
#         banned.sort()  # Sort the banned list
#         curr = 0  # Pointer for the banned list

#         for i in range(1, n + 1):  # Iterate through [1, n]
#             if curr < len(banned) and i == banned[curr]:
#                 curr += 1  # Skip banned numbers
#                 continue
#             if ans + i > maxSum:  # Stop if adding `i` exceeds maxSum
#                 break
#             ans += i  # Update the sum
#             pick += 1  # Increment the count

#         return pick

class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        current_sum = 0
        count = 0

        for num in range(1, n + 1):
            if num in banned_set:
                continue
            if current_sum + num > maxSum:
                break
            current_sum += num
            count += 1

        return count
