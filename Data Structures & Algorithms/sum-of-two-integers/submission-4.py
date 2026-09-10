class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0 
        mask = 0xFFFFFFFF

        # input 1 + 1
        for i in range(32):
            a_bit = (a >> i) & 1 # 1  0
            b_bit = (b >> i) & 1 # 1  0 
            cur_bit = a_bit ^ b_bit ^ carry # 0  1 
            carry = (a_bit + b_bit + carry) >= 2  # 2 (1 + 1 + 0) 1 ( 0 + 0 + 1)
            if cur_bit: # False True
                res |= (1 << i) # 0010 
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res
