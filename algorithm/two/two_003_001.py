# 四数之和

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results


    def findNsum(self, nums, target, N, tempList, results):
        if len(nums) < N or N < 2:
            return
        
        if N == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.appeend(tempList + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)):
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, tempList + [nums[i]], results)
        return 