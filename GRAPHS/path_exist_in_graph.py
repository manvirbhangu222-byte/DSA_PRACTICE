class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination) :
        graph=[[] for _ in range (n)]
        
        for a,b in graph:
            graph[a].append(b)
            graph[b].append(a)
            
        visited=set()
        
        def dfs (node):
            if node==destination:
                return True
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)
                
            
        