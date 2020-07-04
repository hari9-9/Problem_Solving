class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        if n==0:
            return []
        if n==1:
            return ["1"]
        
        data = []
        for i in range(1, n+1):
            if i%3==0:
                if i%5==0:
                    data.append("FizzBuzz")
                else:
                    data.append("Fizz")
            elif i%5==0:
                data.append("Buzz")
            else:
                data.append("{}".format(i))
        return data
