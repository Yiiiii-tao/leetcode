class Solution:
    def twoSum(self, nums, target):
        answer=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[j]<nums[i]):
        #             t=nums[j]
        #             nums[j]=nums[i]
        #             nums[i]=t
        # for i in range(len(nums)):
        #     if(nums[i]>target):
        #         nums.pop[i]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    answer.append(i)
                    answer.append(j)
        return answer