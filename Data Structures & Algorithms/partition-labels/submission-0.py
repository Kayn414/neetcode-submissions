class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        res = []
        count = 0
        seen = set()
        start = 0

        for i, c in enumerate(s):
            freq[c] -= 1
            seen.add(c)

            if all(freq[ch] == 0 for ch in seen):
                res.append(i - start + 1)
                start = i + 1 
                seen.clear()
        
        return res