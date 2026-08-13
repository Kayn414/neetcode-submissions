class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        max_freq = 0
        max_len = 0
        
        vocab = set(s)
        if len(vocab) == 1:
            return len(s)

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
        
            max_len = max(max_len, right - left + 1)
        
        return max_len