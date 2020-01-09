class Solution:
    def isPalindrome(self, sl: list) -> int:
        sll = len(sl)
        for i in range(int((sll / 2))):
            print(str(sl[i]) + " - " + str(sl[sll-i-1]))
            if sl[i] != sl[(sll-i-1)]:
                    return 1
        return 0

    def wherePalindrome(self, sl: list) -> list:
        even = []
        odd  = []
        for i in range((len(sl) - 1)):
            if sl[i] == sl[i+1]:
                even.append(i)
            if i == 0:
                continue
            else:
                if sl[i-1] == sl[i+1]:
                    odd.append(i)

        return [even, odd]

    def lengthPalindrome(self, sl: list, where: int, what: int) -> int:
        if what == 0:
            length = 2
            left  = (where -1)
            right = (where + 2)
            while (left >= 0) and (right < len(sl)) and (sl[left] == sl[right]):
                length = length + 2
                left = left - 1
                right = right + 1
        else:
            length = 3
            left = (where - 2)
            right = (where + 2)
            while (left >= 0) and (right < len(sl)) and (sl[left] == sl[right]):
                length = length + 2
                left = left - 1
                right = right + 1

        return length

    def cutPalindrome(self, sl: list, where: int, length: int) -> str:
        #print("length: " + str(length))
        if ((length) % 2) == 0:
            #print("even")
            left  = int(where - (length / 2) + 1)
            right = int(where + (length / 2) + 1)
            #print("left and right: " + str(left) + " - " + str(right))
            return "".join(sl[left:right])
        else:
            #print("odd")
            left  = int(where - int(length / 2))
            right = int(where + int(length / 2) + 1)
            #print("left and right: " + str(left) + " - " + str(right))
            return "".join(sl[left:right])



    def longestPalindrome(self, s: str) -> str:
        sl = list(s)
        if len(sl) == 0:
            return str(s)
        temp = self.wherePalindrome(sl)
        even = temp[0]
        odd  = temp[1]
        max = 0
        sub = -1
        for i in range(len(even)):
            #print("start: " + str(sl[even[i]]) + " - " + str([even[i]]))
            temp = self.lengthPalindrome(sl, even[i], int(0))
            if temp > max:
                max = temp
                sub = even[i]
        for i in range(len(odd)):
            #print("start: " + str(sl[odd[i]]) + " - " + str([odd[i]]))
            temp = self.lengthPalindrome(sl, odd[i], int(1))
            if temp > max:
                max = temp
                sub = odd[i]
        #print("result: " + str(max) + " - " + str(sub))
        if max > 0:
            return self.cutPalindrome(sl, sub, max)
        else:
            return "".join(sl[0])


solution = Solution()
#print(str(solution.isPalindromic("abcbaa")))
#print(str(solution.longestPalindrome("abcbaa")))
print(str(solution.wherePalindrome(list("abaaaa"))))
print(str(solution.longestPalindrome("abaaaa")))
print(str(solution.wherePalindrome(list("abcdcbaaa"))))
print(str(solution.longestPalindrome("abcdcbaaa")))
print(str(solution.wherePalindrome(list(""))))
print(str(solution.longestPalindrome("")))
