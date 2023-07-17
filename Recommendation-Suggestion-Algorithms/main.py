from algorithms.cosine_similarity import cosine_similarity
from algorithms.pearson_correlation_coefficient import pearson_similarity
from algorithms.get_recommendation import get_recommendations1
from algorithms.get_recommendation import get_recommendations2

if __name__ == "__main__":
    # Sample movie ratings dataset
    ratings = {
        'Alice': {'Movie1': 5, 'Movie2': 4, 'Movie3': 3, 'Movie4': 4},
        'Bob': {'Movie1': 3, 'Movie2': 4, 'Movie3': 5, 'Movie5': 4},
        'Charlie': {'Movie1': 4, 'Movie3': 2, 'Movie5': 3},
        'David': {'Movie2': 5, 'Movie3': 1, 'Movie4': 4, 'Movie5': 2},
    }

    user = 'Alice'
    recommendations1 = get_recommendations1(user, ratings, pearson_similarity)
    recommendations2 = get_recommendations1(user, ratings, cosine_similarity)

    print(f"Movie recommendations for {user}:")
    for (movie, score) in recommendations1:
        print(f"{movie}: {score:.2f}")

    for (movie, score) in recommendations2:
        print(f"{movie}: {score:.2f}")