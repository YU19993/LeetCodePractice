#Reverse Integer
#Given a 32-bit signed integer, reverse digits of an integer.

#Assume we are dealing with an environment which could only store
#integers within the 32-bit signed integer range: [−2**31,  2**31−1].
#For the purpose of this problem, assume that your function returns 0
#when the reversed integer overflows.

#Example 1:
#Input: 123
#Output: 321

#Example 2:
#Input: -123
#Output: -321

#Example 3:
#Input: 120
#Output: 21

class Solution:
    def neatInteger(self, x: list) -> int:
        if x[0] == '-':
            while x[1] == 0:
                x.pop(1)
        else:
            while x[0] == 0:
                x.pop(0)
        target =  int("".join(x))
        #check output ovewrflow
        if ((target > int(2147483647)) or (target < int(-2147483648))):
            return 0
        return target


    def reverse(self, x: int) -> int:
        #check input overflow
        if ((int(x) > int(2147483647)) or (x < int(-2147483648))):
            return 0
        if x > 0:
            #[::-1] reverse string
            return self.neatInteger(list(str(x)[::-1]))
        else:
            return self.neatInteger((['-'] + list(str(abs(x))[::-1])))
