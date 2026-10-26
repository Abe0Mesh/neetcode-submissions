class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Main thing I need to do is track the two operands that we are going to use for a operator

        op = []
        
        for t in tokens:
            if t == '+':
                op.append(op.pop() + op.pop()) # op = [1,2] this does append (3) so op would be 3
            
            elif t == '-':
                op.append(op.pop(-2) - op.pop()) # 1 2, -> 2 - 1

            elif t == '/':
                # need to make sure we are ceieling/rounding to 0 for negative division
                if op[-2] / op [-1] >= 0:
                    op.append(op.pop(-2) // op.pop())
                else:
                    op.append(-(op.pop(-2) // -op.pop()))



                

            elif t == '*':
                op.append(op.pop() * op.pop())
            
            else:
                # numbers/operands added to stack
                op.append(int(t))

        return op.pop()
        