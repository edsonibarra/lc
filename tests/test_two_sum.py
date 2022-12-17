import pytest
from src.challenges.two_sum import two_sum, two_sum_2

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2,7,11,15], 9, [[0,1], [1,0]]),
        ([3, 5, 8], 11, [[0, 2], [2, 0]]),
        ([3,2,4], 6, [[1,2], [2,1]]),
        ([3,3],6,[[0,1],[1,0]])
    ]
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums=nums, target=target) in expected
