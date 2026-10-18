class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # input: AB 
        # counts -> {A: 1, B:1}
        counts = Counter(tiles)
    
        # call_1: res += 1 
        def backtrack():
            res = 0
            for c in counts:
                if counts[c] > 0:
                    counts[c] -= 1
                    res += 1 
                    res += backtrack()
                    counts[c] += 1
            return res 

        return backtrack()

