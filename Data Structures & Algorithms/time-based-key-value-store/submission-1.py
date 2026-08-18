class TimeMap:

    def __init__(self):
        self.time = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        
        if key not in self.time:
            return ""
        
        pairs = self.time[key]
        low, high = 0, len(pairs) - 1
        res = ""

        while low <= high:
            mid = low + (high - low) // 2
            mid_ts, mid_val = pairs[mid]

            if mid_ts == timestamp:
                return mid_val
            elif mid_ts < timestamp:
                res = mid_val
                low = mid + 1
            else:
                high = mid - 1

        return res



