# 四数之和
# 这个问题要求在一个数组中找到所有和为给定目标值的四个数的组合，并且每个组合中的数字不能重复使用。

class Solution:
    # res: 存储所有满足条件的组合
    # nums：输入的数组
    # n 数组的长度
    # tempList：正在构建的组合
    # remain：当前组合的剩余目标值（即还需要多少才能达到目标值）
    # start: 当前递归的起时位置，用于避免重复使用数字
    # hashmap：用于去重的哈希表，存储已经找到的组合
    def backtrack(self, res, nums, n, tempList, remain, start, hashmap):
        if len(tempList) > 4:
            # 如果当前组合的长度大于4，直接返回；因为我们想要的是4个数的组合
            return
        
        if remain == 0 and len(tempList) == 4:
            if str(tempList) in hashmap:
                return
            else:
                hashmap[str(tempList)] = True
                res.append(tempList.copy())
                return
            
        for i in range(start, n):
            tempList.append(nums[i])
            self.backtrack(res, nums, n, tempList, remain - nums[i], i + 1, hashmap)
            tempList.pop()

    def fourSum(self, nums, target):
        res = []
        hashmap = {}
        nums.sort()
        self.backtrack(res, nums, len(nums), [], target, 0, hashmap)
        return res
    
# 测试代码
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = solution.fourSum(nums, target)
    print("结果:", result)
