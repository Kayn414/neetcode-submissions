class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))

        for ch in range(len(t_sorted)):
            if s_sorted[ch] != t_sorted[ch]:
                return False

        return True