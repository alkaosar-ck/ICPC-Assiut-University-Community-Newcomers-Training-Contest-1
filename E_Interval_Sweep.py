# a, b = map(int, input().split())
# if (abs(a - b) <= 1) and (a > 0 or b > 0):
#     print('YES')
# else:
#     print('NO')
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mi = min(arr)
        mx = max(arr)
        target = x

        if x < mi:
            n = [arr[i] for i in range(k)]
            return sorted(n)
        elif x > mx:
            l = arr[::-1]
            n = [l[i] for i in range(k)]
            return sorted(n)
        elif k == 1 and target not in arr:
           side_arr = arr.append(target)
           side_arr = sorted(side_arr)
           index_i = side_arr.index(target)
           test1 = side_arr[index_i-1]
           test2 = side_arr[index_i+1]
           if abs(test1 - target) < abs(test2 - target):
               new.append(test1)
           elif abs(test1 - target) > abs(test2 - target):
               new.append(test2)
           else:
               new.append(min(test2, test1))
           
        else:
            side = k // 2
            index = arr.index(target)
            new = [arr[index]]

            for i in range(1, side + 1):
                if index - i >= 0:
                    new.append(arr[index - i])
            for i in range(1, side + 1):
                if index + i < len(arr):
                    new.append(arr[index + i])

            if len(new) == k:
                return sorted(new)
            else:
                i_of_min = arr.index(min(new))
                i_of_max = arr.index(max(new))
                test1 = None
                test2 = None

                if i_of_max + 1 < len(arr):
                    test1 = arr[i_of_max + 1]
                if i_of_min - 1 >= 0:
                    test2 = arr[i_of_min - 1]

                if test1 is not None and test2 is not None:
                    if abs(test1 - target) < abs(test2 - target):
                        new.append(test1)
                    elif abs(test1 - target) > abs(test2 - target):
                        new.append(test2)
                    else:
                        new.append(min(test2, test1))
                elif test1 is not None:
                    new.append(test1)
                elif test2 is not None:
                    new.append(test2)

                new = sorted(new[:k])
                return new
