class Solution:
    def checkPossibility(self, nums):
        flag=1
        s=len(nums)
        for i in range(1,s):
            if(nums[i]>=nums[i-1]):
                continue
            if(i==1):
                flag-=1
                nums[i-1]=nums[i]
            elif(i==s-1):
                nums[i]=nums[i-1]
                flag-=1
            else:
                if(nums[i-1]<=nums[i+1]):
                    nums[i]=nums[i-1]
                    flag-=1
                else:
                    if(nums[i]>nums[i-2]):
                        nums[i-1]=nums[i]
                        flag-=1
                    else:
                        return False
            if(flag==-1):
                return False
        return True
def main():
    s=Solution()
    print(s.checkPossibility([3,4,2,3]))
if __name__ == '__main__':
    main()