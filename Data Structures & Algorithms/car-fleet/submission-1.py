class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = [] #stores the times to target per car

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s) #don't want int division
            #make sure there's at least 2 elements/cars in stack
            #must be less equal because the faster one (-2) will catch up to slower (-1)
            #as a result, it'll join the fleet, decreasing total number of fleets
            #cuz otherwise it would be all individual cars as fleets
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack) #fleetcount is the number of cars 
