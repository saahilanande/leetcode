class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]   #make a stack
        closetoopen={"}":"{","]":"[",")":"("} #make a hashmap for brackets with closing brackets as a key
        
        for x in s: 
            if x in closetoopen: #if a close bracket exsist in the stack
                if stack and stack[-1]==closetoopen[x]: #check if stack is not empty and the top of the stack contains the opening bracket
                    stack.pop()
                else: #if it does not then return false
                    return False
            else:
                stack.append(x) #if the first item is open bracket the push in stack
                
        return True if not stack else False