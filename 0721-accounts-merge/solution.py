class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name 

            for email in account[2:]:
                graph[first_email].add(email)
                graph[email].add(first_email)

        visited = set()
        result = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)

        for email in email_to_name:
            if email not in visited:
                component = []

                dfs(email, component)

                component.sort()

                result.append(
                    [email_to_name[email]] + component
                )

        return result