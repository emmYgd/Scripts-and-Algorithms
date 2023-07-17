import numpy as np
from collections import defaultdict
from typing import *

def pearson_similarity(user1: Dict, user2: Dict) -> float | int:
    # Get common movies and ratings
    common_data_set: Set = set(user1.keys()) & set(user2.keys())

    if not common_data_set:
        return 0

    user1_ratings: Iterable = np.array([user1[movie] for movie in common_data_set])
    user2_ratings: Iterable = np.array([user2[movie] for movie in common_data_set])

    # Calculate the Pearson correlation coefficient
    mean1: float | int = np.mean(user1_ratings)
    mean2: float | int= np.mean(user2_ratings)
    std1: float | int = np.std(user1_ratings)
    std2: float | int = np.std(user2_ratings)

    if std1 == 0 or std2 == 0:
        return 0

    normalized_user1: float = (user1_ratings - mean1) / std1
    normalized_user2: float = (user2_ratings - mean2) / std2

    similarity: float = np.dot(normalized_user1, normalized_user2) / len(common_data_set)

    return similarity

