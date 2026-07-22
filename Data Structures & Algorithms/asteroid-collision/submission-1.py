class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = asteroids[:]

        while True:
            collision = False
            i = 0

            while i < len(arr) - 1:
                if arr[i] > 0 and arr[i + 1] < 0:

                    if abs(arr[i]) > abs(arr[i + 1]):
                        arr.pop(i + 1)

                    elif abs(arr[i]) < abs(arr[i + 1]):
                        arr.pop(i)

                    else:
                        arr.pop(i + 1)
                        arr.pop(i)

                    collision = True
                    break

                i += 1

            if not collision:
                break

        return arr