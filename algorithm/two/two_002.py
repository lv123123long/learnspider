# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []

        # 为什么找到n-2个数就可以了，因为后面的两个数是由前面的数组成的
        # 当前元素， 左指针元素，右指针元素，如果遍历到倒数第一个，第二个元素，就没有足够的元素组成三元组了
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:   # 检查左指针元素是否重复
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
    
import unittest

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_case2(self):
        nums = []
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_case3(self):
        nums = [0]
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_case4(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_case5(self):
        nums = [-1, 0, 1, 0]
        expected = [[-1, 0, 1]]
        self.assertEqual(self.solution.threeSum(nums), expected)

if __name__ == '__main__':
    unittest.main()
