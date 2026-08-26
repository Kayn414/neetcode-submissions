class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i):
            if not digits:
                return []

            if i == len(digits):
                res.append("".join(curr))
                return
            
            digit = digits[i]
            for letter in phone[digit]:
                curr.append(letter)
                backtrack(i + 1)
                curr.pop()

        
        backtrack(0)
        return res