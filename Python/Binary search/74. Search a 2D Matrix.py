class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        
        bottom = len(matrix)-1
        
        while top <= bottom:
            
            mid = (top + bottom)//2
            
            if target < matrix[mid][0]:
                
                bottom = mid - 1
                
            elif target > matrix[mid][-1]:
                
                top = mid + 1
                
            else:
                
                break
                
        if not (top<=bottom):
            return False
        
        col = len(matrix[0])
        
        row = (top + bottom)//2
        
        l = 0
        
        r = col -1
        
        while l <= r :
            m = (r + l)//2
            
            if target < matrix[row][m]:
                r = m - 1
            
            elif target > matrix[row][m]:
                l = m + 1
                
            else:
                return True
            
        return False