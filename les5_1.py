from typing import List, Optional

some_list = [1, 2, 3, [11, 21, 31, [22, 33]], 1, 1, [[[44, 45]]]]

result = [1, 2, 3, 11, 21, 31, 22, 33, 1, 1, 44, 45]


def flat_list(data: List[list]) -> List[int]:
    result = []
    for itm in data:
        if isinstance(itm, list):
            result.extend(flat_list(itm))
        else:
            result.append(itm)
        return result


some_result = flat_list(some_list)


def flat_list1(data: List[list]) -> List[int]:
    for itm in data:
        if isinstance(itm, list):
            yield from flat_list(itm)
        else:
            yield itm
    return result


some_result = list(flat_list1(some_list))
