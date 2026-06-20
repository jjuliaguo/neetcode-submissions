class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashS = {}
        for index1 in range(len(s)):
            hashS[s[index1]] = 1 + hashS.get(s[index1], 0) #make sure it's not hashS[index1]
        
        for index2 in range(len(t)):
            if t[index2] not in hashS:
                return False
            else:
                hashS[t[index2]] -= 1
                if hashS[t[index2]] == 0:
                    del hashS[t[index2]]
            
        return True