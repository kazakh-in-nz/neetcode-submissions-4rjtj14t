class Solution:
    def _mustCollide(self, a1: int, a2: int) -> bool:
        return a1 > 0 and a2 < 0

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            if len(s) == 0 or not self._mustCollide(s[-1], a):
                s.append(a)
                continue

            needToAppend = False

            while len(s) > 0 and self._mustCollide(s[-1], a):
                needToAppend = False

                if abs(s[-1]) == abs(a):
                    s.pop()
                    break

                if abs(s[-1]) > abs(a):
                    break

                if abs(s[-1]) < abs(a):
                    s.pop()
                    needToAppend = True
            else:
                if needToAppend:
                    s.append(a)

            # if len(s) == 0 and needToAppend:
            #     s.append(a)

        return s
