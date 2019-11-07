class Solution:
    def minSubArrayLen(self, s, nums):
        # min = len(nums)
        # a = 0
        # if(len(nums)):
        #     sums = [nums[0]]
        #     for i in range(1, len(nums)):
        #         sums.append(sums[i - 1] + nums[i])
        # for i in range(len(nums)):
        #     index = 0
        #     for j in range(i, len(nums)):
        #         sum = sums[j] - sums[i] + nums[i]
        #         if (sum >= s):
        #             index = j - i + 1
        #             break
        #     if (min >= index and sum >= s):
        #         min = index
        #         a = sum
        # if (min == len(nums) and a < s):
        #     min = 0
        # return min
#my own solution time limit exceeded
        window_start, window_end, l = 0, 0, len(nums)
        window_sum = 0
        min_length = l + 1
        for window_end in range(l):
            window_sum += nums[window_end]
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                if min_length == 1:
                    break
                window_sum -= nums[window_start]
                window_start += 1
        return min_length if min_length <= l else 0
    #sliding window solution
def main():
    a=Solution()
    print(a.minSubArrayLen(15,[1,2,3,4,5]))
if __name__ == '__main__':
    main()