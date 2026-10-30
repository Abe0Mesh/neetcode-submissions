class Solution:
    def isPalindrome(self, s: str) -> bool:

        # skip non alpha numeric,  

        s.strip()
        i = 0
        j = len(s) - 1
        # WasitacaroracatIsaw?"
        while i < j:
            
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[j].lower() != s[i].lower():
                return False 

            i += 1
            j -= 1
        
        return True
        