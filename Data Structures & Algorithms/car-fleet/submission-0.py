class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = [] #stores the times to target per car

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s) #don't want int division
            #make sure there's at least 2 elements/cars in stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack) #fleetcount is the number of cars 
