class NumArray:

    def __init__(self, nums: List[int]):
        self.num_array = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num_array[left:right+1])
