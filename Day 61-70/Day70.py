# https://www.geeksforgeeks.org/problems/leaf-at-same-level/1


class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        #Code here
        def height(node, hgt, cnt):
            if not node:
                return
            if not node.left and not node.right:
                hgt.append(cnt)
                cnt = 0
            height(node.left, hgt, cnt+1)
            height(node.right, hgt, cnt+1)
        hgt = []
        height(root, hgt, 1)
        if len(list(set(hgt))) > 1:
            return False
        else:
            return True
