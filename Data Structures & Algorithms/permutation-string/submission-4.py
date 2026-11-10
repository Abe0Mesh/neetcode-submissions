class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        map1 = {}
        for s in s1:
            map1[s] = map1.get(s, 0) +1
        
        i = 0
        map2 = {}
        for j in range(0, len(s2)):

            map2[s2[j]] = map2.get(s2[j], 0) + 1

            if j >= len(s1) - 1:

                if map1 == map2:
                    return True
                # else
                map2[s2[i]] = map2.get(s2[i]) - 1 # now we are shifting window so we dec that val 
                if map2[s2[i]] == 0:
                    del map2[s2[i]]
                i += 1


        
        return False
