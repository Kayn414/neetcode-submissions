class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []                      

        for j, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                i = stack.pop()
                res[i] = j - i         
            stack.append(j)

        return res