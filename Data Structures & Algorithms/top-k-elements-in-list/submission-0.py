class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    #create a hashmap that stores the amt of times a number appears
    #you're gonna store the numbers that appear the same amt of times 
    #together using the same key (the freq the appear at)
    #create a while loop based on k
    #use an index (use max function)
    #decrement the ks as u continue moving down
    #return the list of values

#nums

#count frequencies
 
#frequency dictionary
 
#build buckets
 
#scan buckets from high frequency to low frequency

        frequency = {}

        for num in nums:
            if num in frequency: #if exists as a key
                frequency[num] += 1
            else:
                frequency[num] = 1
        temp = 1
        arr = []
        while temp <= len(nums):
#add all of the nums that correspond to temp freq
            for item in frequency:
                if frequency[item] == temp:
                    arr.append(item)
            temp+=1
    
    #builds incrementing array

        return arr[len(arr)-k:]
