class NumericalArray:
    """
    A class to represent a numerical array.
    
    Example:
    numArray = NumericalArray([-2, 0, 3, -5, 2, -1])
    numArray.sumRange(0, 2)  # returns 1
    numArray.sumRange(2, 5)  # returns -1
    numArray.sumRange(0, 5)  # returns 3

    """
    def __init__(self, nums: List[int]):
        self.num_array = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num_array[left:right+1])
