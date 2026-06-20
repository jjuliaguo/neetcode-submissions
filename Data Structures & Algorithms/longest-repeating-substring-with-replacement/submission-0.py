class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #use sliding window to count number of 'not same' chars
        #if the two char counts are the same, doesn't matter what replaces what
        #probably use a hashmap to count freq

        #note: string can't be empty (at least 1)

        #ex2:
        #right pointer will keep incrementing as long as tempK > k
        #the number of replacements are 

        exists = {}
        maxLength = 0
        l = 0 #guaranteed smallest length 1

        for r in range(len(s)):
            exists[s[r]] = exists.get(s[r], 0) + 1
            windowSize = r - l + 1
            maxFreq = max(exists.values())
            #while loop is flipped
            while windowSize - maxFreq > k: #not valid
                exists[s[l]] -= 1
                if exists[s[l]] == 0:
                    del exists[s[l]]
                l += 1
                windowSize = r - l + 1
                maxFreq = max(exists.values())
            #if valid
            #exists[s[r]] = exists.get(s[r], 0) + 1
            #maxLength = max(exists.values())
            maxLength = max(maxLength, r-l+1)
            
        return maxLength