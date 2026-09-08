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
            l = i+1 
            r = len(nums)-1 
            while l<r: 
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] == target:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in result:
                        result.append(triplet)
                    l += 1
                    r -= 1 # moving inwards not making it outwards still
                    #the array is sorted so by moving l inwards, it gets larger
                    #so yk the last index cant be at the end bcuz that's going to
                    #be larger than the previous one that sufficed
                else:
                    l+=1
        
        return result


    