class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #to check if char alr exists there
        charSet = set()
        l = 0
        res = 0 #longest substring w/o repeating chars

        for r in range(len(s)): #the for loop is essentially right pointer
            while s[r] in charSet: #need a while loop bcuz u keep removing until no dupe
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1) #make sure to +1 
        return res