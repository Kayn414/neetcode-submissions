class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # ['c', 'a', 't'] 0 -> c, 1 -> a, 2-> t
        n = len(s)
        l,r = 0, n - 1
        while l <= r:
            if s[l] != s[r]:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
            else:
                l += 1
                r -= 1
        
            
                    
    
        
        