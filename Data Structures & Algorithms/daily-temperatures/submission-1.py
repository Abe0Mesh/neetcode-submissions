class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        # temps [3,2,4] 
        # res = [0,0,0]

        # i = 0
        # s[0]

        # i = 1
        #2 > 3 NO
        # s[0,1]

        # i = 2
        # 4 > 2 -> yes pop 1 from stack
        # s[0]
        # res = [0,1,0]
        # loop again
        # 4 > 3, true we pop 0, 2-0 = 2, 
        # res = [2, 1, 0]
        

        result = [0 for i in temperatures] 

        for i in range(0, len(temperatures)):
            # start by checking the top of the stack
            # we check if this new temp is

            # need to make sure s isnt empty
            if s: 

                while s and temperatures[i] > temperatures[s[-1]]: # new temp > top of stack
                    pop = s.pop() 
                    result[pop] = i - pop  # new index - compared inex = days gap 

            s.append(i) 


        return result