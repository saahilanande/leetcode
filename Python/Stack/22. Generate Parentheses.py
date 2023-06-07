class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        
        result = []
        
        def recursioncheck(openbracket,closebracket):
            if openbracket == closebracket == n:
                result.append("".join(stack))
                return 
            
            if openbracket<n: # if number of open brackets are less that the given count
                stack.append("(") # append a open bracket to stack
                recursioncheck(openbracket+1,closebracket) #recall the method with updated open bracket counts
                stack.pop() #remove the top bracket
                
            
            if openbracket > closebracket: #if open brackets are more than close bracket in stack
                stack.append(")") #append a close bracket to the stack
                recursioncheck(openbracket,closebracket+1) #Update the close bracket count
                stack.pop()
                
        recursioncheck(0,0)
        return result