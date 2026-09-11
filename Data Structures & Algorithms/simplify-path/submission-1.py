class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        bucket = []

        for i, d in enumerate(directories):
            if d == "" or d == ".":
                continue

            if d == "..":
                if bucket:
                    bucket.pop()
                continue

            bucket.append(d)

        return "/" + "/".join(bucket)