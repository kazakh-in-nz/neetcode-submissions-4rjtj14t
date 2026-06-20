class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            alive = True

            while s and s[-1] > 0 and a < 0:
                if abs(s[-1]) < abs(a):
                    s.pop()
                    continue
                elif abs(s[-1]) == abs(a):
                    s.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                s.append(a)

        return s
