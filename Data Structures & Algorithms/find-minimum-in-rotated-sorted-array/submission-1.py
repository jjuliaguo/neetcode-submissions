class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #rotating len(nums) makes it original array
        # this is trivial: return min(nums)

        l, r = 0, len(nums) - 1
        in_order = sorted(nums)
        min = float("inf")

        while l<=r:
            mid = (l+r)//2
            #1, 2, 3, 4
            if in_order[mid] < min:
                min = in_order[mid]
                r = r - 1
            else:
                r = r - 1

        return min