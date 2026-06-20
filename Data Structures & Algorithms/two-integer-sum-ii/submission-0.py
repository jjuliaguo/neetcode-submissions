class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
       #carefully read the instructions (non-dec order is important)

       l = 0
       r = len(numbers) - 1
       result = [0] *2

       while r>l:
        #if sum larger than target then u keep going down
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] == target:
            result[0] = l + 1
            result[1] = r + 1
            return result
        else:
            l += 1


