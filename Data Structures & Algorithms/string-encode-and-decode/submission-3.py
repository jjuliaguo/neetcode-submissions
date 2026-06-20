class Solution:

    def encode(self, strs: List[str]) -> str:

        #after every word, you add a .

        result = ""
        for s in strs:
            result += s
            result += "."
        return result

    def decode(self, s: str) -> List[str]:
        out = []
        l, r = 0, 0 
        while r < len(s):
            if s[r] == ".":
                out.append(s[l:r])
                l = r+1
                r += 1
            else:
                r += 1
        return out

