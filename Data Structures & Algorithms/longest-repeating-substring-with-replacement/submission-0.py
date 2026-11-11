class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        char_count = {}
        max_len = 0
        
        i = 0
        for j in range(len(s)):

            char_count[s[j]] = char_count.get(s[j], 0) + 1 # we count freqs here


            if (j - i + 1) - max(char_count.values()) > k:
                # this means substirng still valid with repalcement
                # We also dont need to track if the elems are the saem as huighest freq is enought o tell us
                char_count[s[i]] -= 1
                i += 1

        


            if max_len < (j - i + 1):
                max_len = j - i + 1


        
        return max_len




            # remeeber to dec freqeunces wehn moving i / changing window
        