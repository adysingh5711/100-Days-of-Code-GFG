# https://www.geeksforgeeks.org/problems/is-it-a-tree/1


class Solution:
    def isCyclePresent(self,node,adj,vis,p):
        vis.add(node)
        for i in adj[node]:
            if i not in vis:
                if not self.isCyclePresent(i,adj,vis,node): return 0
            elif i!=p: return 0
        return 1
    def isTree(self, n, m, edges):
        # Code here
        adj,vis=[[]for _ in range(n)],set()
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        b=self.isCyclePresent(0,adj,vis,-1)
        if len(vis)!=n: return 0
        return b
