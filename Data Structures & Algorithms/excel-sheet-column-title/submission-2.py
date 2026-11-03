class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        temp = columnNumber
        tempS = ""
        while temp > 26:
            temp -= 1
            resVal = temp % 26
            tempS += chr(resVal + 65) 
            temp = (temp - resVal) // 26
        temp -= 1
        tempS += chr(int(temp) + 65)
        result = ""
        for i in range(len(tempS) - 1, -1, -1):
            char = tempS[i]
            result += char
        return result