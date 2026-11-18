import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        rules
        - 1 hour 1 pile
        Goal: return lowest Banana Per Hour rate (k)

        brute force:
        find max pile - M
        loop 1 to M 
        each loop have another loop check if each pile can be eaten within time block, 
        return first num (as we are going from accedning) that works within time limit

        optimization:
        - instead of checking each k value, we use a bin search
        - 
        '''

        
        l = 1
        r = max(piles)
        k = 0
        min_k = r



        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            # 2 takes 6 hours [1,4,3,2], h = 9, [1]

            if hours <= h: # too fast
                # slower
                r = k - 1
                min_k = min(k, min_k)
            if hours > h:
                # faster
                l = k + 1


        return min_k
                

        