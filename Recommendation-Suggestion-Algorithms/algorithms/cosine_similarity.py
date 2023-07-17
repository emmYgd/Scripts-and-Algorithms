from typing import *
import math

def cosine_similarity(user1: Dict, user2: Dict) -> float | int:
    common_data_set: Set = set(user1.keys()) & set(user2.keys())

    if not common_data_set:
        return 0

    sum1: float | int = sum(user1[movie] for movie in common_data_set)
    sum2: float | int = sum(user2[movie] for movie in common_data_set)

    sum1_sq: float | int = sum(user1[movie] ** 2 for movie in common_data_set)
    sum2_sq: float | int = sum(user2[movie] ** 2 for movie in common_data_set)

    num: float | int = sum1 * sum2
    den: float | int = math.sqrt(sum1_sq * sum2_sq)

    if den == 0:
        return 0

    return num / den