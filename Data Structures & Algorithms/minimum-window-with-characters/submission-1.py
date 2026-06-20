class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, there's nothing to search for
        if t == "":
            return ""

        # countT stores how many of each character we NEED
        countT = {}

        # window stores how many of each character are CURRENTLY
        # inside our sliding window
        window = {}

        # Build the frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have = number of unique characters we've satisfied
        # need = total number of unique characters we must satisfy
        have = 0
        need = len(countT)

        # Store the best (smallest) window found so far
        res = [-1, -1]
        resLen = float("infinity") #resLen = len(s) + 1

        # Left pointer of the sliding window
        l = 0

        # Expand the window by moving the right pointer
        for r in range(len(s)):

            # Current character entering the window
            c = s[r]

            # Add it to the window frequency map
            window[c] = 1 + window.get(c, 0)

            # If this character now has exactly enough copies,
            # we've satisfied one required character
            if c in countT and window[c] == countT[c]:
                have += 1

            # If we've satisfied every required character...
            while have == need:

                # Check if this window is the smallest valid one
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                    #if (r - l + 1) < resLen:
                    #resLen = r - l + 1
                    #res = [l, r]

                # Remove the leftmost character from the window
                window[s[l]] -= 1

                # If removing it means we no longer have enough
                # of that required character, the window becomes invalid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Shrink the window from the left
                l += 1

        # Extract the best window found
        l, r = res 

        # If no valid window was ever found, return ""
        # Otherwise return the substring
        return s[l:r+1] if resLen != float("infinity") else "" 
        # if resLen == len(s) + 1:
        # return ""