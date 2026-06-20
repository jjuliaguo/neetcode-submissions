class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # if empty or 1 number, return false immediately

        if len(nums) <= 1:
            return False

        # convert into hash set
        numMap = set()

        #you don't care abt the index so dont do range(len(nums))
        for index in nums:
            #search for the value in hash table

            #first check if number is in hashset already
            #if so, then it's a duplicate
            if index in numMap:
                return True

            # if not found, add to hash table
            else:
                numMap.add(index)

        return False