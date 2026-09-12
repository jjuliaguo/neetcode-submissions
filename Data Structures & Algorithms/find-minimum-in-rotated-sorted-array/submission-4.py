class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[0]

        while l<=r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                mini = min(mini, nums[r])
                l = mid+1
                #5,1,2,3,4
            elif nums[mid] <= nums[r]: 
                mini = min(mini, nums[mid])
                r = mid - 1

        return mini