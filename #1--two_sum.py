class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        for i, j in enumerate(nums):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[j] = i
