class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        ans = self.q[0]
        self.q.append(self.q.popleft())   
        return ans

    def empty(self) -> bool:
        return len(self.q) == 0