l ,r = 0 , len(height)-1

    # O(n)
        maxout = 0
        
        while l<r:
            lowestheight = min(height[l],height[r])
            maxout = max(maxout,lowestheight*(r-l))
            
            if height[l]<height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
        return maxout
        
    # O^2

        maxout = 0
        
        for x in range(len(height)):
            for j in range(x+1,len(height)):
        
                lowestheight = min(height[x],height[j])
                maxout = max(lowestheight*(j-x),maxout)
            
        return maxout