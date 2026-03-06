class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)


        reverse = defaultdict(list)


        outdegree = [0] * n

        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reverse[v].append(u)

        queue = deque()

        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = []

        while queue:
            node = queue.popleft()
            safe.append(node)


            for prev in reverse[node]:
                outdegree[prev] -= 1

                if outdegree[prev] == 0:
                    queue.append(prev)

        return sorted(safe)