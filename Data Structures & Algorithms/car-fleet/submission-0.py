class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

                # carfleet equiv to destination time

        
        # car with highest postion will stay ahead.

        # (pos, speed)
        # pos : 1, speed 3, so we know target - pos, = rem, rem/speed = time to reach. 
        # pos 1, speed 3 so 10-1 = 9 / 3 = at 3 hours 
        # pos 4, sped 2, so 10-4 = 6 / 2 = 3

        # here we would check the highesrt positoin, and its est 3.5, so any position lower then 3 with a est > 3.5 is set to 3.5

        # (pos, final time)
        s = [(position[i], (target - position[i]) / speed[i]) for i in range(0, len(position))]
        s.sort()



        # [4 "3", 1 "3"]

        fleets = 0
        while s:
            cur = s.pop()[1]
            fleets += 1
            while s and s[-1][1] <= cur: # So while c's est is > any cars in stacks
                s.pop()


        return fleets


        # highest pos first, 

