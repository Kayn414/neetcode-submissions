class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = deque()    

        if k == 1:
            res.append(max(freq, key=freq.get))
            return list(res)


        sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        for num in sorted_nums:
            res.append(num)

        while len(res) > k:
            res.pop()          

        return list(res) 
