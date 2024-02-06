# https://www.geeksforgeeks.org/problems/node-at-distance/1


class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def dfs(self,root,stack,k,vis):
        if root:
            stack.append(root)
            if not root.left and not root.right:
                n=len(stack)
                if n>k and (stack[-k-1] not in vis):
                    vis.add(stack[-k-1])
            self.dfs(root.left,stack,k,vis)
            self.dfs(root.right,stack,k,vis)
            stack.pop()
    
    def printKDistantfromLeaf(self, root, k):
        vis=set()
        self.dfs(root,[],k,vis)
        return len(vis)
