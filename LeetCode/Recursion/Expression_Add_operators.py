class Solution:
    def solve(self, num, i, path, curr_value, prev_value, target, ans):
        if i == len(num):
            if curr_value == target:
                ans.append("".join(path))
            return

        for j in range(i, len(num)):
            temp = num[i:j+1]

            # Avoid numbers with leading zeros
            if len(temp) > 1 and temp[0] == "0":
                continue

            number = int(temp)

            if i == 0:
                # First number in expression, start without an operator
                self.solve(num, j+1, path + [temp], number, number, target, ans)
            else:
                # Addition
                self.solve(num, j+1, path + ["+", temp], curr_value + number, number, target, ans)

                # Subtraction
                self.solve(num, j+1, path + ["-", temp], curr_value - number, -number, target, ans)

                # Multiplication (adjust previous value for correct precedence)
                self.solve(num, j+1, path + ["*", temp], curr_value - prev_value + (prev_value * number), prev_value * number, target, ans)

    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        self.solve(num, 0, [], 0, 0, target, ans)
        return ans
