class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #try using the prefix suffix approach

        pre = [0] * len(nums)
        suf = [0] * len(nums)
        result = [0] * len(nums)
        index = 0
        tempProd = 0

        #remember the enumerate function
        for ind in range(len(nums)): #why not enumerate?
            if ind == 0:
                pre[ind] = 1
            else:
                pre[ind] = pre[ind-1] * nums[ind-1]

            
        #suffix loop
        for ind2 in range(len(nums)-1, -1, -1):
            if ind2 == len(nums)-1:
                suf[ind2] = 1
            else: 
                suf[ind2] = suf[ind2+1] * nums[ind2+1]
        
        for indFinal in range(len(result)):
            result[indFinal] = pre[indFinal] * suf[indFinal]

        return result
