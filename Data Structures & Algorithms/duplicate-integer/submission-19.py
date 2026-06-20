class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #runtime explanation

        # We iterate through the array once, 
        # so the loop runs n times. Inside each iteration, 
        # we perform a hash set lookup and insertion, 
        # both of which are O(1) on average. 
        # Therefore the total runtime is O(n). 
        # The hash set may store every unique element, 
        # so in the worst case it uses O(n) additional space.

        values = set()

        for item in nums:
            if item in values:
                return True

            else:
                values.add(item)

        return False