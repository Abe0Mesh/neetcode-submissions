class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        for j in range(len(s1) - 1, len(s2)):
            i = j - len(s1) + 1

            # checking if this cur window has the same elms of s1
            # if so imm return true else continue looping

            # while loop comparing sorted list i-j, and sorted s1
            # so a substring i to j sorted vs s1 sorted

            sub2 = sorted(s2[i:j+1])
            sub1 = sorted(s1)

            if sub1 == sub2:
                return True


        
        return False
