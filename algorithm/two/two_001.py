# 两数之和 ， 给一个数组 一个目标值，输出相加等于目标值的两个数的下标
# 例如：输入[2, 7, 11, 15]，目标值9，输出[0, 1]

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        mapper = {}         # 辅助使用的hash表，key是nums[i]，value是i 
        for i in range (n):
            if target - nums[i] in mapper:
                return [mapper[target - nums[i]], i]
            else:
                mapper[nums[i]] = i
        return []
    

import unittest

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_case3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_case4(self):
        nums = [1, 2, 3, 4, 5]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [3, 4])

    def test_case5(self):
        nums = [1, 2, 3, 4, 5]
        target = 7
        self.assertEqual(self.solution.twoSum(nums, target), [2, 3])

if __name__ == '__main__':
    unittest.main()
