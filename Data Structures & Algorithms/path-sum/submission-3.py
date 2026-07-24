
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [root]
        visited = [False]
        localSum = 0

        while stack:
            curr, isVisited = stack.pop(), visited.pop()

            if curr:
                if isVisited:
                    if localSum == targetSum and not curr.left and not curr.right:
                        return True

                    localSum -= curr.val

                else:
                    stack.append(curr)
                    localSum += curr.val
                    visited.append(True)

                    stack.append(curr.right)
                    visited.append(False)
                    
                    stack.append(curr.left)
                    visited.append(False)
        
        return False

        