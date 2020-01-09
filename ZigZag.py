#ZigZag Conversion

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass
        where = []
        target = ""
        for i in range(numRows):
            where.append(int(i))
        for i in range(1, (numRows - 1)):
            where.append(int(numRows - i - 1))

        wl = len(where)
        for i in range(numRows):
            for ii in range(len(s)):
                if where[ii % wl] == i:
                    target = target + s[ii]
        return target

solution = Solution()
print(solution.convert("PAYPALISHIRING", 4))
print("PINALSIGYAHRPI")
