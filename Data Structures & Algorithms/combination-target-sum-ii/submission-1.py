class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def backtrack(i, remainder):        
            if remainder == 0:
                res.append(curr.copy())
                return
            if remainder < 0 or i == len(candidates):
                return 
            
            curr.append(candidates[i])
            backtrack(i + 1, remainder - candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # skip dups
                i += 1
            backtrack(i + 1, remainder)

        backtrack(0, target)
        return res