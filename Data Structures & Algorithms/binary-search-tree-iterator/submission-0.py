# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.p = 0
        self.ordered_arr = []

        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.ordered_arr.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        if self.p < len(self.ordered_arr):
            output = self.ordered_arr[self.p]
            self.p += 1
            return output
        else:
            return -1
        

    def hasNext(self) -> bool:
        return self.p < len(self.ordered_arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()