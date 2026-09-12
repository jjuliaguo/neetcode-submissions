#this is straightforward bcuz ur not tracking the min

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r: #not <= because it relies on all numbers being unique
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
                #5,1,2,3,4
            elif nums[mid] < nums[r]: 
                r = mid #not mid-1 in case mid is smallest

        return nums[l]