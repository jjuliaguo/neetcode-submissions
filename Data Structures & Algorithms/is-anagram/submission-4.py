class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anaT = {}
        for i in range(len(t)):
            #remember t is a string so you're not assigning i to large index
            #therefore, not anaT[i] = t[i]
            if t[i] in anaT:
                anaT[t[i]] += 1
            else:
                anaT[t[i]] = 1

        for i in range(len(s)):
            if s[i] in anaT:
                #to remove, you can't use del since it deletes the entire thing:
                #needs to be s[i] and not t[i] because you're finding the letter to dec
                anaT[s[i]] -= 1
                #also should add this, make sure it doesn't keep dec
                if anaT[s[i]] < 0:
                    return False
            else:
                return False
        return True
        