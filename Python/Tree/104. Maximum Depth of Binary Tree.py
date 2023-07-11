# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## DFS Recursive
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        # ## BFS Iteravtive
        # que = deque()
        # if root:
        #     que.append(root)

        # level = 0

        # while que:
        #     for i in range(len(que)):
        #         node = que.popleft()
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        #     level += 1
        
        # return level


        # DFS Iterative
        stack = [[root,1]]
        maxlevel = 0

        if not root:
            return maxlevel

        while stack:
            node,level = stack.pop()
            
            if node:
                maxlevel = max(level,maxlevel)
                stack.append([node.left,level + 1])
                stack.append([node.right,level + 1])
            
        return maxlevel