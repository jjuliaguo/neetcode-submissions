class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # if empty or 1 number, return false immediately

        if len(nums) <= 1:
            return False

        # convert into hash table
        numMap = {}

        for index in range(len(nums)):
            #search for the value in hash table

            #if found return true and stop
            if nums[index] in numMap:
                return True

            # if not found, add to hash table
            else:
                numMap[nums[index]] = index

        return False