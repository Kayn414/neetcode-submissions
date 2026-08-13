class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = Counter(s1)
        sub_2 = Counter()
        left = 0
        for right in range(len(s2)):
             sub_2[s2[right]] += 1 #  Add the new character

             # Keep the window size equal to len(s1)
             while right - left + 1 > len(s1):
                 sub_2[s2[left]] -= 1
                 if sub_2[s2[left]] == 0:
                     del sub_2[s2[left]]
                 left += 1

             if sub_2 == sub:
                 return True

        return False
    