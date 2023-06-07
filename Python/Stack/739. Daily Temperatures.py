class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #pair:[index, value] monotonic decreasing stack

        for i, t in enumerate(temperatures): 
            while stack and stack[-1][0] < t: #if the current value is greater than top of the stack
                stackValue, stackIndex,  = stack.pop() #pop the less value
                res[stackIndex] = i - stackIndex #get the difference and add to result array
            stack.append((t,i)) #if the current value is less that top of stack then add that value with index

        return res