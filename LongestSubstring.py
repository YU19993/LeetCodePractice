#3. Longest Substring Without Repeating Characters
#Given a string, find the length of the longest substring without repeating characters.

#Example 1:

#Input: "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#1: break a string into several substings by repeated character
#2:compare length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = list(s) #seperate string into list
        sub = []
        at = 0
        max = 0
        while at < len(sl):
            if not sl[at] in sub:
                sub.append(sl[at])
                at = at + 1
                if len(sub) > max:
                    max = len(sub)
            else:
                if len(sub) > 0:
                    sub.pop(0)
        return max


solution = Solution()
print(str(solution.lengthOfLongestSubstring("dvdf")))
print(str(solution.lengthOfLongestSubstring("abcabcbb")))
