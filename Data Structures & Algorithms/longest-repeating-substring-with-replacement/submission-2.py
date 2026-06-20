class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        exists = {} 
        maxLength = 0 
        l = 0 

        for r in range(len(s)):
            exists[s[r]] = exists.get(s[r], 0) + 1 
            windowSize = r - l + 1
            maxFreq = max(exists.values()) # this is not optimal cuz looks through all of exist

            while windowSize - maxFreq > k: 
                exists[s[l]] -= 1 
                #bcuz i do exists.values(), it checks entire thing, so we'd had to delete
                #I delete keys whose count becomes 0 so the hashmap only contains characters that are actually in the current window.
                #but if use optimal version, you don't need to delete all the 0s
                #maxFreq is maintained separately
                if exists[s[l]] == 0: 
                    del exists[s[l]] 
                l += 1
                windowSize = r - l + 1
                maxFreq = max(exists.values())

            maxLength = max(maxLength, r-l+1)

        return maxLength