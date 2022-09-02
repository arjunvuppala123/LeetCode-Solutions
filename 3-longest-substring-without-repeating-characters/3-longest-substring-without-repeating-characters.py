class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLen,length = 0,0
        count = {}
        
        for i in range(len(s)):
            if s[i] in count and currLen <= count[s[i]]:
                currLen = count[s[i]] + 1
            else:
                length = max(i-currLen+1,length)
            count[s[i]] = i
        
        return length