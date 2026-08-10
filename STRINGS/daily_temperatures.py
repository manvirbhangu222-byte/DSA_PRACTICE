class Solution(object):
    def dailyTemperatures(self, temperatures):
        res=[0]* len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[ stack[-1]]:
                previous_day=stack.pop()
                res[previous_day]=i-previous_day
            stack.append(i)
        return res