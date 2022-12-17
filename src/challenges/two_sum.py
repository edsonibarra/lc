"""
Link to challenge: https://leetcode.com/problems/two-sum
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Complexity:
        Time O(n)
        Space O(n)
    """
    seen = dict()
    for i, n in enumerate(nums):
        result: int = target - n
        if result in seen:
            return [i, seen[result]]
        seen[n] = i

def two_sum_2(nums: List[int], target: int) -> List[int]:
    """

    Note: This will only work when you are asked for the numbers intead of
    the indices.

    Complexity:
        Time O(nLog(n))
        Space O(1)
    """
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


