class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        start = 0

        for i in range(len(gas)):
            net = gas[i] - cost [i]
            tank += net
            total += net

            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1