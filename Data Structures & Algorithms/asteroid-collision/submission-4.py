class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            alive = True

            while len(s) > 0 and s[-1] > 0 and a < 0 and alive:
                if abs(s[-1]) > abs(a):
                    alive = False
                    break

                if abs(s[-1]) == abs(a):
                    alive = False

                s.pop()
                
            if alive:
                s.append(a)

        return s
        