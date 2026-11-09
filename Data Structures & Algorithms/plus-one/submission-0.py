class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = True
        for i in range(len(digits) - 1, -1 , -1):
            print("fuckyou")
            if add == False:
                break
            else:
                add = False
            digit = digits[i]


            if digit + 1 >= 10:
                add = True
                digits[i] = 0
            else:
                print(" i is now " + str(digit + 1))
                digits[i] = digit + 1
                add = False
                break
        if add == True:
            result = [1]
            for i in range(len(digits)):
                digit = digits[i]
                result.append(digit)
            return result
        else:
            return digits