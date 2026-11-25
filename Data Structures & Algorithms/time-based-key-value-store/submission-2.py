class TimeMap:
    '''
    Goal:  Make a time based map 1 key with mutliple time+ val combos

    brute force:
    use a dict to store key vals key = [(time, val)]
    then for gettign we go and search all tuples and see if there time < time asked

    optimziation:
    Instead of checking every time we know that times are accending because time moves forward
    We can use a binary search due to the list being in accending order
    allowing us to search in o(log n ) time to find the value closest to the target
    target = timestamp 

    Inside bin search loop
    we set a middle

    we check if mid > target:
        mid is too big and isnt valid, move right to the left of mid
        r = mid - 1

    [1,4,8, 10, 40, 80] times
    target = 30,
    we know everyhring 30 and less is valid and we want closest tough so we 
    dont want to disinclude mid if its < target, so 
    if mid <= target
        move left TO mid, which would give us the biggest time while still valid

    '''

    def __init__(self):
        self.m = {} 
        # if we want data for alice = [] stores a list of (time,val) tuples


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append( (timestamp, value) ) # apending to keep accending time order
        
    # key1: val1:10, get key1,10
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        vals = self.m[key]


        l = 0
        r = len(vals) - 1
        closest_index = -1
        while l <= r:
            mid = (l + r) // 2
            mid_time = vals[mid][0]
            if mid_time > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                closest_index = max(closest_index, mid)

        if closest_index == -1:
            return ""
        return vals[closest_index][1] 
    


        
