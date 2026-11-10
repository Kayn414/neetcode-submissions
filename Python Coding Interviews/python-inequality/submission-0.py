from typing import List


def is_arr_valid(names: List[str], max_length: int) -> bool:
    is_greater = False
    for name in names:
        if 0 < len(name) <= max_length:
            is_greater = True
    return is_greater



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
