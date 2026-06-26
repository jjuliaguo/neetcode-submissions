class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #start from the end of temperatures (beginning of stack)
        #go through using a for/while loop through indexes of negative
        #peek at the numbers and if 
        #the warmer one should be larger 
        #if added to results array, pop it off

       stack = []
       result = [0] * len(temperatures)

        #do this so you can access the index
        #stores it as (index, temp) in the stack
       for index, temp in enumerate(temperatures):
        #remember: there's no peek() function 
        while stack and stack[-1][1] < temp:
            prev = stack.pop()
            result[prev[0]] = index - prev[0] 
            #we don't have to add it back onto the stack
            #because the while loop handles all the elements' comparison
        
        stack.append((index, temp)) #this has to be outside the while loop (because it's already fixed)
        
       return result 

       #runtime:
       #Although there's a nested while loop inside the for loop, 
       #each temperature is pushed onto the stack exactly once and 
       #popped at most once

