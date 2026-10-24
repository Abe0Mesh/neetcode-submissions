class MinStack:

    def __init__(self):
        self.sk = []
        self.min_sk = []

    
        

    def push(self, val: int) -> None:
        if not self.min_sk:
            self.min_sk.append(0)
            
        elif val < self.sk[self.min_sk[-1]]:
            # To track the index's of the smallest items, and when we pop we check if that index is in min_sk
            # min_sk would be orded by min values and to get the min value index
            self.min_sk.append(len(self.sk))
        self.sk.append(val) 





        

    def pop(self) -> None:
        if self.min_sk[-1] == len(self.sk) - 1:
            self.min_sk.pop()
        self.sk.pop()

        

    def top(self) -> int:
        return self.sk[-1]
        

    def getMin(self) -> int:
        return self.sk[self.min_sk[-1]]
        
