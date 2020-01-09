#Validate if a given string can be interpreted as a decimal number.

#Some examples:
#"0" => true
#" 0.1 " => true
#"abc" => false
#"1 a" => false
#"2e10" => true
#" -90e3   " => true
#" 1e" => false
#"e3" => false
#" 6e-1" => true
#" 99e2.5 " => false
#"53.5e93" => true
#" --6 " => false
#"-+3" => false
#"95a54e53" => false

# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
# However, here is a list of characters that can be in a valid decimal
# number:
#
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."

class Solution:

    def isI(self, c: str) -> bool:
        if c == "0" or c == '1' or c == '2' or c =='3' or c == '4' or c == '.'\
            or c == '5' or c =='6' or c == '7' or c =='8' or c == '9':
            return True
        return False

    #find the position and number of "e"
    def findE(self, s: list) -> list:
        num = 0
        where = -1
        for i in range(len(s)):
            if s[i] == "e":
                num = num + 1
                where = i
        return [num, where]

    #find the position and number of "e"
    def findD(self, s: list) -> list:
        num = 0
        where = -1
        for i in range(len(s)):
            if s[i] == ".":
                num = num + 1
                where = i
        return [num, where]

    def isN(self, s: list) -> bool:
        #find Numbber of '.'
        d = self.findD(s)
        #error: have more than one .
        if d[0] > 1:
            return False
        sl = s
        #error: only "+" or "-"
        if sl[0] == '-' or sl[0] == '+' or sl[0] == '.':
            if len(sl) == 1:
                return False
        #valid number string
        if sl[0] == '-' or sl[0] == '+' or self.isI(sl[0]):
            if sl[0] != '+':
                target = [sl[0]]
            else:
                target = []
            for i in range(1, len(sl)):
                if self.isI(sl[i]):
                    target.append(sl[i])
                # elif sl[i] == ' ':
                #     continue
                else:
                    return False
            #no number captured
            if len(target) == 0:
                return False
            #error: only "-"
            elif len(target) == 1 and target[0] == '-':
                return False
            elif len(target) == 2 and target[0] == '-' and target[1] == '.':
                return False
            return True
        else:
            return False


    def isNumber(self, s: str) -> bool:
        s = list(s)
        if len(s) == 0:
            return False
        while s[0] == ' ':
            s.pop(0)
            if len(s) == 0:
                return False
        while s[(len(s) - 1)] == ' ':
            s.pop((len(s) - 1))
            if len(s) == 0:
                return False
        #first check e
        e = self.findE(s)
        if e[0] > 1:
            return False
        elif e[0] == 1:
            where = e[1]
            if where == s[0] or where == s[(len(s) - 1)]:
                return False
            else:
                s1 = s[0:where]
                s2 = s[(where + 1): len(s)]
                if len(s1) == 0 or len(s2) == 0:
                    return False
                i =  self.findD(s2)
                if i[0] != 0:
                    return False
                if self.isN(s1) and self.isN(s2):
                    return True
                else:
                    return False
        elif e[0] == 0:
            d = self.findD(s)
            if d[0] > 1:
                return False
            else:
                return self.isN(s)
        else:
            return False


sol = Solution()
# print(str(sol.findE("e123ess")))
print(str(sol.isNumber(" -.")))
#"2e10" => true
#" -90e3   " => true
#" 1e" => false
#"e3" => false
#" 6e-1" => true
#" 99e2.5 " => false
#"53.5e93" => true
#"95a54e53" => false
