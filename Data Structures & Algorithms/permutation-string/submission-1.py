class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #permutation = same letters, must be consecutive, different ordering allowed
        #guaranteed at least 1 in both s1 and s2

        #create a hashmap for s1
        #use the for r in range
        #check if in hashmap of s1, 
        #then use while element is not in hashmap-> the invalid case is if they're not permutations
            # l += 1
            # add the freq of s2[l] by 1 -> dont think needed bcuz the dec comes after
        #otherwise, 
            #dec the freq of that element by 1
            # increment right pointer
        # return True
        if len(s2) < len(s1):
            return False
        if len(s1) == 0 or len(s2) == 0:
            return False

        required = {}
        current = {}
        l=0

        #sets up same sized sliding window
        for i in range(len(s1)):
            required[s1[i]] = 1 + required.get(s1[i], 0)

        for r in range(len(s2)): #(0, len(s2)-len(s1)+1): #starts where current ends off, goes up until start of last window, inc by s1 length each time
            current[s2[r]] = 1 + current.get(s2[r], 0)

            if r-l+1 > len(s1): # if window too large, remove leftmost
                current[s2[l]] -= 1

                if current[s2[l]] == 0:
                    del current[s2[l]]
                l+=1

            if required == current:
                return True
            

        return False

                   

        #come back to it
        #maybe implement 2 hash maps for both s1 and s2 instead
        #15 mins