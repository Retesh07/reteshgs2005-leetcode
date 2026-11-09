import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        counts = [0] * k

        available = list(range(k))
        heapq.heapify(available)

        busy = []

        for h, (a, l) in enumerate(zip(arrival, load)):

            while busy and busy[0][0] <= a:
                finish, server = heapq.heappop(busy)
                heapq.heappush(available, h + (server - h) % k)

            if not available:
                continue

            server = heapq.heappop(available) % k

            counts[server] += 1

            heapq.heappush(busy, (a + l, server))

        maxi = max(counts)

        return [i for i, x in enumerate(counts) if x == maxi]