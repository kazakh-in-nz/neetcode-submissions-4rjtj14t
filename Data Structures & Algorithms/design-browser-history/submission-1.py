class Node:
    def __init__(self, page: str):
        self.page = page
        self.next, self.prev = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        page = Node(url)
            
        self.curr.next, page.prev = page, self.curr
        self.curr = page

    def back(self, steps: int) -> str:
        curr = self.curr
        i = 0

        while curr.prev and i < steps:
            i += 1
            curr = curr.prev

        self.curr = curr
        return curr.page

    def forward(self, steps: int) -> str:
        curr = self.curr
        i = 0

        while curr.next and i < steps:
            i += 1
            curr = curr.next

        self.curr = curr
        return curr.page        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)