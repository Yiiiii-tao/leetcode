class Solution:
    def lengthOfLongestSubstring(self, s) :
        max=-1
        for i in range(len(s)):
            longestindex=-1
            longest = []
            longeststr=''.join(longest)
            for j in range(i,len(s)):
                if(longeststr.find(s[j])==-1):
                    longestindex+=1
                    longest.append(s[j])
                    longeststr = ''.join(longest)
                else:
                    break
            if(max<longestindex):
                max=longestindex
        return max+1
def main():
    a=Solution()
    print(a.lengthOfLongestSubstring('abcdeabc'))
if __name__ == '__main__':
    main()

