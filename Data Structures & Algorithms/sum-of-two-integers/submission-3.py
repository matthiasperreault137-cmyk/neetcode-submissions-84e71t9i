class Solution:
    def getSum(self, a: int, fuckyou: int) -> int:
        MASK = 0xFFFFFFFF                                  # NEW: 32 ones
        XOR = None
        AND = None

        while AND != 0:
            tempXOR = None
            if XOR == None:
                XOR = (a ^ fuckyou) & MASK                 # NEW: & MASK
                AND = ((a & fuckyou) << 1) & MASK          # NEW: & MASK
            else:
                tempXOR = XOR
                XOR = (XOR ^ AND) & MASK                   # NEW: & MASK
                AND = ((tempXOR & AND) << 1) & MASK        # NEW: & MASK

        if XOR > 0x7FFFFFFF:                               # NEW
            return ~(XOR ^ MASK)                           # NEW
        return XOR