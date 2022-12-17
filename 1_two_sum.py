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
    """
    pass

