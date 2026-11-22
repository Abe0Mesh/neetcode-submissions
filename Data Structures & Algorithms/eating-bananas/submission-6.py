import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        Goal: Find lowest valid bannas per hour eating rate (k)

        brute force:
        1- max(bananPile):
        for each banana eating rate check the time it would take to eat the banannas and if its valid compared to h rate    

        optimization:
        Instead of brute force going through every k value we can use binary search to move quickly through k values
        '''


        # piles=[1,4,3,2] k's = 1,2,3,4
        # mid = 2
        # 1 + 2 + 2 + 1 time is 6
        # 

        
        r = max(piles)
        l = 1
        best_k = r
        # So we loop 1-max, each iteration we check the time cost to eat bananas at i rate
        while l <= r:
            mid_k = (r + l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/mid_k) # pile is 5, k is 2 > time = 3

            if time <= h: # if time is valid but also means all to the right could be valid but would be bigger k 
                best_k = min(mid_k, best_k)
                r = mid_k - 1            # so no need to check them we got the best k from that sub window
                
            
            # so if time slow time (time > h) then from mid and left wont work and invalid
            else:
                l = mid_k + 1
        return best_k
                


# brute force

        # m = max(piles)
        # # So we loop 1-max, each iteration we check the time cost to eat bananas at i rate
        # for k in range(1, m + 1):

        #     time = 0
        #     for p in piles:
        #         time += math.ceil(p/k) # pile is 5, k is 2 > time = 3

        #     if time <= h: # if time is valid
        #         return k

        

        