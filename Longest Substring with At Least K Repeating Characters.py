class Solution:
    def longestSubstring(self, s,k):
        behind=[]
        max=0
        lens=0
        window_start,window_end=0,0
        for i in range(len(s)):
            behind.append(0)
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    behind[i]+=1
        dict={}
        while window_end<len(s):
            if(s[window_end]not in dict.keys()):
                dict[s[window_end]]=1
                if(window_end==len(s)-1):
                    flag = 1
                    for i in dict.keys():
                        if (dict[i] < k):
                            flag = 0
                    if (flag == 1):
                        lens = window_end - window_start + 1
                    if (lens > max):
                        max = lens
                if(behind[window_end]<k-1):
                    flag='#'
                    dict.pop(s[window_end])
                    for i in dict.keys() :
                        if(dict[i]<k):
                            flag=i
                            break
                    if(flag=='#'):
                        lens=window_end-window_start
                        window_start = window_end + 1
                        if (lens > max):
                            max = lens
                    else:
                        for i in range(window_start,window_end):
                            if(s[i]==flag):
                                lens=i-window_start
                                if(lens>max):
                                    max=lens
                                flagIndex=i
                                break
                        window_start=flagIndex+1
                        window_end=flagIndex
                    dict.clear()
            else:
                dict[s[window_end]] = dict[s[window_end]]+1
                if(window_end+1==len(s)):
                    flag=1
                    for i in dict.keys():
                        if(dict[i]<k):
                            flag=0
                    if(flag==1):
                        lens=window_end-window_start+1
                    if(lens>max):
                            max=lens
            window_end+=1
        return max
    def longestSubstring1(self, s, k):
            if len(s) == 0:
                return 0
            d = {}
            for l in s:
                try:
                    d[l] += 1
                except:
                    d[l] = 1
            stop = []
            for key in d.keys():
                if d[key] < k:
                    stop.append(key)
            if len(stop) == 0:
                return len(s)
            valid_s = []
            start = 0
            for i in range(len(s)):
                if s[i] in stop:
                    valid_s.append(s[start:i])
                    start = i + 1
            valid_s.append(s[start:])
            max_v = 0
            for vs in valid_s:
                if len(vs) == 0:
                    continue
                tmp = self.longestSubstring1(vs, k)
                if tmp > max_v:
                    max_v = tmp
            return max_v
def main():
    s=Solution()
    print(s.longestSubstring1('ababacb',3))
if __name__ == '__main__':
    main()