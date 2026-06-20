class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #limiting factor = shorter bar

        resultMax, tempMax = 0, 0

        l, r = 0, len(heights)-1

        while l != r:
            width = r-l
            height = min(heights[l], heights[r])

            tempMax = width * height

            if tempMax > resultMax:
                resultMax = tempMax
                tempMax = 0
            
            if heights[l] >= heights[r]: #if equal, doesn't matter what pointer gets changed
                    r -= 1
            else:
                    l +=1
        
        return resultMax