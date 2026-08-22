from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque((i, ticket) for i, ticket in enumerate(tickets))
        s = 0
        while q:
            i, e = q.popleft()
            e -= 1
            s += 1

            if i == k and e == 0:
                return s
            if e > 0:
                q.append((i, e))

        return s



