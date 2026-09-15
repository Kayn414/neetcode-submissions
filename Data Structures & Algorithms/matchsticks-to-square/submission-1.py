class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0 or len(matchsticks) < 4:
            return False
        
        length = total // 4
        if max(matchsticks) > length:
            return False
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= matchsticks[i]
                if sides[side] == 0:
                    break
            
            return False
        
        return dfs(0)
                    

                