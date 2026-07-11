class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        complete_components_count = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True

                vertex_count = 0
                edge_count = 0

                while queue:
                    curr = queue.popleft()
                    vertex_count += 1

                    edge_count += len(adj[curr])

                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                if edge_count == vertex_count * (vertex_count -1):
                    complete_components_count += 1
        return complete_components_coun
