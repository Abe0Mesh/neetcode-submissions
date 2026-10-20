class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = {}
        for key in freq.keys():
            v = freq[key]
            if v not in sorted_freq:
                sorted_freq[v] = []
                sorted_freq[v].append(key)
            else:
                sorted_freq[v].append(key)

        # k = 3

        fin = []
        sfk = list(sorted_freq.keys())
        sfk.sort(reverse=True)

        count = 0
        for f in sfk:
            if count == k:
                break
            for num in sorted_freq[f]:
                fin.append(num)
                count += 1

        return fin
            