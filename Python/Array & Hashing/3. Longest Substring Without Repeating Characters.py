class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Sliding window

        char = set()

        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            r +=1
            res=max(res, r - l)
        return res