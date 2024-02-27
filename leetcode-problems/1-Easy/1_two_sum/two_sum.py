"""
LeetCode two sum problem (Easy)
"""


class TwoSum(object):
    """two sum solution"""

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                j += 1
        return indices
