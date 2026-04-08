class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def _insert(self, root, n):
        if not root:
            return n

        if root.key < n.key:
            root.right = self._insert(root.right, n)
        elif root.key > n.key:
            root.left = self._insert(root.left, n)
        else:
            root.val = n.val
        return root
        
    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(self.root, Node(key, val))

    def _search(self, root, target):
        if not root:
            return -1

        if root.key < target:
            return self._search(root.right, target)
        elif root.key > target:
            return self._search(root.left, target)
        else:
            return root.val

    def get(self, key: int) -> int:
        return self._search(self.root, key)

    def _getMin(self, root) -> Node:
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr if curr else None

    def getMin(self) -> int:
        n = self._getMin(self.root)

        return n.val if n else -1

    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right

        return curr.val if curr else -1

    def _remove(self, root, key):
        if not root:
            return None

        if root.key > key:
            root.left = self._remove(root.left, key)
        elif root.key < key:
            root.right = self._remove(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minRight = self._getMin(root.right)
                root.val = minRight.val
                root.key = minRight.key
                root.right = self._remove(root.right, minRight.key)

        return root

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        results = []

        def dfs(root):
            if not root:
                return


            left = dfs(root.left)
            results.append(root.key)
            right = dfs(root.right)

        dfs(self.root)

        return results

