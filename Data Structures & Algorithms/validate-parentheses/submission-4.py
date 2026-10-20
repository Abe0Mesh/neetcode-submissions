class Solution:
    def isValid(self, s: str) -> bool:

        # we add all opens to the stack and when we see a clseod we pop it
        stack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            else:
                if not stack:
                    return False
                popped = stack.pop()

                if p == '}':
                    if popped != '{':
                        return False

                elif p == ')':
                    if popped != '(':
                        return False
                
                elif p == ']':
                    if popped != '[':
                        return False
                

        if not stack:
            return True
        return False
