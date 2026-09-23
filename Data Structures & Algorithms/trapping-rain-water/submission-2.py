class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)
        total = 0
        i = 0

        while i < n - 1:
            # 1. Find the left wall of the next bucket
            #    (first place that is higher than the next bar)
            while i + 1 < n and height[i] <= height[i + 1]:
                i += 1
            left = i

            # 2. From here, look for the right wall:
            #    the next bar that is >= height[left]
            #    (or the highest bar we can find if none is tall enough)
            right = left + 1
            max_h = 0
            max_idx = right
            while right < n:
                if height[right] >= height[left]:
                    break                       # found a proper right wall
                if height[right] > max_h:       # keep the highest candidate
                    max_h = height[right]
                    max_idx = right
                right += 1

            # if we never found a bar >= left wall, use the highest one we saw
            if right == n:
                right = max_idx

            # 3. Now we have a bucket [left … right]
            if right > left + 1:
                water_level = min(height[left], height[right])
                width = right - left - 1
                solid = sum(height[j] for j in range(left + 1, right))
                total += water_level * width - solid

            # 4. Move past this bucket and look for the next one
            i = right

        return total
  