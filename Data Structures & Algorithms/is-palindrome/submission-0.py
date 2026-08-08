class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        end = len(s) - 1

        if not s:
            return True

        for i in range(len(s) // 2):
            if s[i] != s[end - i]:
                return False
        return True
