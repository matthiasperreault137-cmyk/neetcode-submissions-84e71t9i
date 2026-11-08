class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            nums = []
            while n != 0:
                nums.append(n % 10)
                n //= 10
            total = 0
            for num in nums:
                total += num * num
            n = total
        if n == 1:
            return True
        else:
            return False