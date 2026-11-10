from typing import List


def create_list_of_odds(n: int) -> List[int]:
    all_odds = [i for i in range(1, n+1, 2)]
    return all_odds


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
