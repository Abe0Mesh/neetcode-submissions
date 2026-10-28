class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Strip the string befor eand get rid of whitespace
        # "tab a cat"
        s.strip()

        # "tabacat" len is 7, 7/2 = 3.5 -> 3 , so 0-2 so t a b, then. 6 , 5 , 4
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i+= 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
        