class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        long = 0
        c_map = {}

        for r in range(len(s)):
            c_map[s[r]] = c_map.get(s[r], 0) + 1

            rep = (r - l + 1) - max(c_map.values())

            while rep > k:
                c_map[s[l]] -= 1
                l += 1
                rep = (r - l + 1) - max(c_map.values())

            long = max(long, (r-l+1))
        return long

        
