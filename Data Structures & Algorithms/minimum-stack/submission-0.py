import heapq
class MinStack:

    def __init__(self):
        self.heap = []
        self.min = heapq.heapify(self.heap)
        self.stack = []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.heap[0] not in self.stack:
            heapq.heappop(self.heap)
        return self.heap[0]
