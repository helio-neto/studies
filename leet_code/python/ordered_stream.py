class OrderedStream:
    """
    OrderedStream is a data structure that receives a stream of (id, value) pairs 
    and returns values in increasing order of their IDs by returning chunks (lists) of values 
    after each insertion.
    
    The concatenation of all the chunks should result in a list of the sorted values.

    Example:
    Your OrderedStream object will be instantiated and called as such:
    obj = OrderedStream(n)
    param_1 = obj.insert(idKey,value)

    """
    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        result = []
        while self.ptr < self.n and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
