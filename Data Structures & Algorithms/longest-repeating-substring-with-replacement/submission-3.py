# Time Complexity

# right pointer work: O(n) -> for loop moves through string once
# left pointer work:  O(n) -> l only moves forward so while loop moves through string once
# total:              O(2n) = O(n)

# Space Complexity
# O(26)
# - The frequency hashmap stores at most 26 uppercase English letters.
# - In the general case (m unique characters), the space complexity is O(m).
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #use sliding window to count number of 'not same' chars
        #if the two char counts are the same, doesn't matter what replaces what
        #probably use a hashmap to count freq

        #note: string can't be empty (at least 1)

        #ex2:
        #right pointer will keep incrementing as long as tempK > k
        #the number of replacements are 

        exists = {} #use freq hashmap
        maxLength = 0 #max length of the window
        l = 0 #guaranteed smallest length 1

        for r in range(len(s)):
            #note: the frequency hashmap gets implemented with the window
            #not before because we need to access maxFreq
            #the character that it is DOESNT matter
            exists[s[r]] = exists.get(s[r], 0) + 1 
            windowSize = r - l + 1
            maxFreq = max(exists.values())

            #while loop is flipped
            #it's the while loop's job to "fix"
            #the for r in range already covers the "valid" indexes by incrementing nontheless
            #but we can't inc if its invalid, so while used to fix
            while windowSize - maxFreq > k: #not valid
                #need this before the if statement
                #bcuz otherwise you'd have elements with counts of 0
                #there won't be a case of negative (if 0 just deleted)
                exists[s[l]] -= 1 
                if exists[s[l]] == 0:
                    del exists[s[l]] #REMEMBER: this deletes entire KEY
                l += 1
                windowSize = r - l + 1
                maxFreq = max(exists.values())

            maxLength = max(maxLength, r-l+1)
            #don't need to inc r because for loop does it

        return maxLength