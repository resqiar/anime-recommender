import math

def cosine_score(current, target):
    # list of common rated anime from current user and target user
    common_anime = {}

    for anime in current["rated"]:
        # if current user rated anime that is also rated by target,
        # add them to common_anime
        if anime in target["rated"]:
            common_anime[anime] = 1

    common_length = len(common_anime)

    # if the length of common anime is 0,
    # meaning that the current and target user has no common anime,
    # return 0 (indicate no similarity between current and target)
    if common_length == 0:
        return 0

    # calculate the X and Y (all ratings in common)
    current_ratings = [float(current["rated"][anime]) for anime in common_anime]
    target_ratings = [float(target["rated"][anime]) for anime in common_anime]

    # calculate the sum of the product
    sum_of_products = sum([rating1 * rating2 for rating1, rating2 in zip(current_ratings, target_ratings)])

    # calculate the sum of squares
    current_squared = sum([rating ** 2 for rating in current_ratings])
    target_squared = sum([rating ** 2 for rating in target_ratings])

    # finally, calculate the cosine similarity
    similarity = sum_of_products / (math.sqrt(current_squared) * math.sqrt(target_squared))

    return similarity
