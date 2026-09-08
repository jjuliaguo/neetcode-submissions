class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #algorithm:
        #start w for loop to set it at i
        #use 2 pointer approach to go through for k and j 
        #check if there have been any dupes
        #if not append it to the result list

        result = []
        l, r, target = 0, 0, 0

        nums.sort()
        #-4, -1, -1, 0, 1, 2
        for i in range(len(nums)):
            target = - nums[i]
            #1
            l = i+1 #2
            r = len(nums)-1 #5
            while l<r: #2<5
                if nums[l] + nums[r] > target: #3 < 4
                    r-=1
                elif nums[l] + nums[r] == target:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in result:
                        result.append(triplet)
                    l += 1
                    r -= 1
                else:
                    l+=1
        
        return result


    