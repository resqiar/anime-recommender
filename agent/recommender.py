from flask import json
from agent.pearson import pearson_score

def get_recommendation(target):
    # open anime data
    with open('data/users.json', 'r') as file:
        # read file as data
        data = json.load(file)

        # Create dictionaries to hold overall and similarity scores
        overall_scores = {}
        similarity_scores = {}

        for current in data["users"]:
            # if the data is current user, skip
            # we dont want to calculate similarity with ourself
            if current["username"] == target["username"]:
                continue

            # calculate similarity using algorithms (pick as needed)
            similarity = pearson_score(current, target)

            # if the similarity score is negative or 0, then skip, 
            # target user has no similarity with current user.
            if similarity <= 0:
                continue

            # loop through each item rated by current user while also
            # not rated by target user
            for anime in current["rated"]:
                if anime not in target["rated"]:
                    # Add anime to the overall score for recommendations
                    overall_scores[anime] = overall_scores.get(anime, 0) + float(current["rated"][anime]) * similarity

                    # Add the similarity to the similarity score for this anime
                    similarity_scores[anime] = similarity_scores.get(anime, 0) + similarity

        # If no recommendations found
        if len(overall_scores) == 0:
            return 0

        # Create a list of anime scores by normalizing overall scores by similarity scores
        anime_scores = [(score / similarity_scores[anime], anime) for anime, score in overall_scores.items()]

        # Sort the list of anime scores in decreasing order
        anime_scores.sort(reverse=True)

        # Extract the recommendations from the sorted list of anime scores
        recommendations = [anime for _, anime in anime_scores]

        return recommendations

    # otherwise return none/null
    return None
