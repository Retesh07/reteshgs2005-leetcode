class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append((v, cost))

        prices = [float("inf")] * n
        prices[src] = 0

        q = deque([(src, 0)])
        stops = 0

        while q and stops <= k:
            size = len(q)

            temp = prices[:]

            for _ in range(size):
                node, cost = q.popleft()

                for nei, price in adj[node]:
                    newCost = cost + price

                    if newCost < temp[nei]:
                        temp[nei] = newCost
                        q.append((nei, newCost))

            prices = temp
            stops += 1

        return -1 if prices[dst] == float("inf") else prices[dst]