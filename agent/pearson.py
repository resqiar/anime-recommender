def pearson_score(current, target):
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

    # formula for pearson_score
    # r = (Σ(x - x̄) (y - ȳ)) / (√Σ(x - x̄)² √Σ(y - ȳ)²)
    # 
    # where x is target?
    # where y is current?

    # calculate the X and Y (all ratings in common)
    current_ratings = [float(current["rated"][anime]) for anime in common_anime]
    target_ratings = [float(target["rated"][anime]) for anime in common_anime]
    
    # calculate the sum for current and target user RATINGS in common
    current_sum = sum(current_ratings)
    target_sum = sum(target_ratings)

    # calculate the sum of squares (this will be used for denominator)
    current_squared = sum([rating ** 2 for rating in current_ratings])
    target_squared = sum([rating ** 2 for rating in target_ratings])

    # calculate sum of the product (sigma?) for current and target
    sum_of_products = sum([rating1 * rating2 for rating1, rating2 in zip(current_ratings, target_ratings)])

    # finally, calculate the formula above
    Sxy = sum_of_products - (current_sum * target_sum / common_length)
    Sxx = current_squared - (current_sum ** 2 / common_length)
    Syy = target_squared - (target_sum ** 2 / common_length)

    # if the denuminator result is 0 return immediately
    if Sxx * Syy == 0:
        return 0

    score = Sxy / ((Sxx * Syy) ** 0.5) 

    return score

