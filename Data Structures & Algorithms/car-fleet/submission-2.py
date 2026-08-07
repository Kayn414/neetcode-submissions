class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p,s) for p, s in zip(position, speed)]

        pos_speed.sort(reverse=True)
        stack = []

        for p,s in pos_speed:
            diff = target - p 
            stack.append(diff / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) 