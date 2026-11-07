class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Immidently I can tell this could easily be solved with a n^2 search
        # But I also think there is a way we can search this O(n)

        # We only need to search left to right once, as the string isnt being modified while we search
        # WHile we loop through this we will track two things Start and END of substring
        l = 0
        nums = set()
        max_sub_s = 0

        for r in range(len(s)): 
            

            if s[r] in nums: # meaning we hit a dupe char
                while s[r] in nums:
                    nums.remove(s[l])
                    l += 1
                    
            nums.add(s[r]) 
            if r - l + 1 > max_sub_s:
                max_sub_s = r - l + 1

        return max_sub_s













               # so I made R (right pointer the main loop asright pointer as end of substring is what matters as by then right cant move anymore no matter what L does

            # Now the thing is we basically DONT want to move L that is our goal
            # WE will attempt to constantly track the longest substring as we go through
        
        # using a set to determine if char is unique

        