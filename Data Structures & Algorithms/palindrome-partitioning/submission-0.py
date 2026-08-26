class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(curr.copy())
                return
            
            for curr_index in range(start, len(s)):
                if isPalindrome(start, curr_index):
                    curr.append(s[start:curr_index+1])
                    backtrack(curr_index + 1)
                    curr.pop()
    
        backtrack(0)
        return res