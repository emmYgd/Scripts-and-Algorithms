from typing import *
from collections import defaultdict

# implementation 1:
def get_recommendations1(user: str, ratings: Dict, similarity_func: float | int) -> List:
    recommendations: DefaultDict = defaultdict(float)

    user_ratings: Dict = ratings[user]
    for (other_user, other_ratings) in ratings.items():
        if other_user == user:
            continue

        similarity: float | int = similarity_func(user_ratings, other_ratings)

        if similarity > 0:
            for item, rating in other_ratings.items():
                if item not in user_ratings or user_ratings[item] == 0:
                    recommendations[item] += similarity * rating

    recommendations: List = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return recommendations


# implementation 2:
def get_recommendations2(user: str, ratings: Dict, similarity_func: float | int):
    recommendations: DefaultDict = defaultdict(float)

    for other_user in ratings:
        if other_user == user:
            continue

        similarity = similarity_func(ratings[user], ratings[other_user])

        if similarity > 0:
            for item in ratings[other_user]:
                if item not in ratings[user] or ratings[user][item] == 0:
                    weight = similarity * ratings[other_user][item]

                    recommendations[item] += weight

    recommendations: List = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return recommendations