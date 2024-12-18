from typing import List
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = []
        for i in range(len(temp)):

            while stack and temp[stack[-1]]< temp[i]:
                old = stack.pop()
                res[old] = i-old 
            stack.append(i)
        return res

# Driver code
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()
    
    # Example input
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    
    # Call the function and print the result
    result = solution.dailyTemperatures(temperatures)
    print("Input temperatures:", temperatures)
    print("Days to wait for a warmer temperature:", result)