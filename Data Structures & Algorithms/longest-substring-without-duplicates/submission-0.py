class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # create an array that stores the characters that have been iterated through so far
        # use l, r pointers and continue going through the string
        # if that letter is in array, return False
        # otherwise, keep going and only inc l once r has hit len(self)-1
        
        #checks empty case
        if not s:
            return 0
        if len(s) == 1: 
            return 1

        l, r = 0, 1 
        resMax, tempMax = 0, 1
        soFar = set()
        
        soFar.add(s[0])
        
        while r < len(s):

            if s[r] not in soFar:
                soFar.add(s[r])
                resMax = max(resMax, r - l + 1)
                r += 1

            else:
                soFar.remove(s[l])
                l += 1

        return resMax
        #while l != r and r < len(s):
            #if s[r] in soFar: #case that it is in
                #if tempMax > resMax:
                    #resMax = tempMax
                    #tempMax = 1
                #l = r + 1
                #r = l + 1
            #else: #case that it isn't
                #tempMax += 1
                #l = r + 1
                #r = l + 1
        

        #return len(soFar)
