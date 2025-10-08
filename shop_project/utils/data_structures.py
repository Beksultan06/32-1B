

from collections import deque


class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)

    def process_next(self):
        if self.queue:
            return self.queue.popleft()