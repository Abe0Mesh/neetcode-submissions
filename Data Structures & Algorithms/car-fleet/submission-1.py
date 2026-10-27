class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(position[i], ((target - position[i]) / speed[i])) for i in range(0, len(position))]
        # cars [(7, 3) , (4, 3) , (1, 4.5) (0, 10)]

        cars.sort()
        
        count = 0 
        while cars:        
            count += 1 
            cur = cars.pop() 
            
            while cars and cur[1] >= cars[-1][1]:
                cars.pop()



        return count

        