class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        seqCounter = 0
        seqLength = []
        for num in numSet:
            if num - 1 not in numSet: # meaning its the start of a seq
                i = 0
                while (num + i in numSet):
                    seqCounter += 1
                    i +=1
                seqLength.append(seqCounter)
                seqCounter = 0


        return max(seqLength)
        