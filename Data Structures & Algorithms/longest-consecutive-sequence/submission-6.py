class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        vals = {}

        if len(nums) != 0:
            maxCount += 1

        for ele in nums:
            if ele in vals:# REMEMBER dont need vals[ele] == ele:
                vals[ele] += 1 #lowk doesn't matter if it exists more than once
            else:
                vals[ele] = 1

        #a number is the start of a sequence if prev number doesn't exist
        #suggested while loop

        for el in nums:
            curr = el
            if curr-1 not in vals:
                count =1 
                while curr+1 in vals:
                    count += 1
                    if count > maxCount:
                        maxCount = count
                    curr += 1
            

        return maxCount