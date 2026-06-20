class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #for the max container, it would be the shorter stick x (distance between the 2 - 1)
        #it only moves on from a bar once every bar has been tested and doesn't increase max amt

        if len(heights) == 0:
            return 0

        resultMax, tempMax = 0, 0
        l, r = 0, 1

        while l<r and r<len(heights):
            length = min(heights[l], heights[r])
            width = r - l #no need -1 since 0 indexed

            tempMax = length * width

            if tempMax > resultMax and r != len(heights)-1:
                resultMax = tempMax
                tempMax = 0
                r += 1
            elif tempMax > resultMax and r == len(heights)-1:
                resultMax = tempMax
                tempMax = 0
                l += 1
                r = l+1
            elif r == len(heights)-1:
                l += 1
                r = l+1
            else:
                r +=1

        return resultMax
