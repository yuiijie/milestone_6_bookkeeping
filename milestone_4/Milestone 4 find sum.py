from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:

    result = []
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                result.append((li[i], li[j]))
    return result

find_sum(5, [1, 2, 3, 4, 5])


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = set()
    result = []

    for num in li:
        complement = target - num
        if complement in seen:
            result.append(tuple(sorted((num, complement))))
        seen.add(num)

    return list(result)

find_sum_fast(5, [1, 2, 3, 4, 5])
