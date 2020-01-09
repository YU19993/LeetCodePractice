#8. String to Integer (atoi)
#Implement atoi which converts a string to an integer.

#The function first discards as many whitespace characters as necessary
#until the first non-whitespace character is found. Then, starting from
#this character, takes an optional initial plus or minus sign followed
#by as many numerical digits as possible, and interprets them as a
#numerical value.

#The string can contain additional characters after those that form the
#integral number, which are ignored and have no effect on the behavior of
#this function.

#If the first sequence of non-whitespace characters in str is not a valid
#integral number, or if no such sequence exists because either str is
#empty or it contains only whitespace characters, no conversion is
#performed.

#If no valid conversion could be performed, a zero value is returned.

#Note:
#Only the space character ' ' is considered as whitespace character.
#Assume we are dealing with an environment which could only store
#integers within the 32-bit signed integer range: [−231,  231 − 1].
#If the numerical value is out of the range of representable values,
#INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def isI(self, c: str) -> bool:
        if c == "0" or c == '1' or c == '2' or c =='3' or c == '4' \
            or c == '5' or c =='6' or c == '7' or c =='8' or c == '9':
            return True
        return False

    def myAtoi(self, str: str) -> int:
        sl = list(str)
        if len(sl) == 0:
            return 0
        while sl[0] == ' ':
            sl.pop(0)
            if len(sl) == 0:
                return 0
        if sl[0] == '-' or sl[0] == '+':
            if len(sl) == 1:
                return 0
        if sl[0] == '-' or sl[0] == '+' or self.isI(sl[0]):
            if sl[0] != '+':
                target = [sl[0]]
            else:
                target = []
            for i in range(1, len(sl)):
                if self.isI(sl[i]):
                    target.append(sl[i])
                else:
                    break
            if len(target) == 0:
                return 0
            elif len(target) == 1 and target[0] == '-':
                return 0
            target = int("".join(target))
            if target > 2147483647:
                target = 2147483647
            elif target < -2147483648:
                target = -2147483648
            return target
        else:
            return 0

sol = Solution()
print(str(sol.myAtoi("  -42")))
print(str(sol.myAtoi("4193 with words")))
print(str(sol.myAtoi("-+2")))
