class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use binary search on every element between 1 and max pile num

        l, r = 1, max(piles)
        answer = max(piles)

        while l<=r:
            mid = (l+r)//2
            if self.canEat(mid, piles) <= h:
                answer = mid #save mid and not self.canEat()
                r = mid - 1
            else:
                l = mid + 1

        return answer

    #checks if this min eating rate is feasible or not
    def canEat(self, speed, piles):
        total = 0
        for i in range(len(piles)):
            total += math.ceil(piles[i]/ speed)

        return total