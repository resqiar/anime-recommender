from flask import Flask, json, jsonify, make_response, render_template, request
from agent.recommender import get_recommendation

app = Flask(__name__)

@app.route("/")
def indexPage():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    return render_template("login.html")

@app.route("/recommendation")
def recommendationPage():
    return render_template("recommendation.html")

@app.route("/history")
def profilePage():
    return render_template("history.html")

@app.route('/rate/<int:id>')
def rate(id):
    # open JSON file
    with open('data/anime.json', 'r') as file:
        # read the file as content
        content = json.load(file)

        # check if logged user is available in the saved data
        for anime in content["animes"]:
            if anime["id"] == id:
                # return their current data
                return render_template("rate.html", anime=anime)

    # otherwise return 404
    return make_response(jsonify({'error': 'anime not found'}), 404)

@app.route("/api/login", methods=['POST'])
def login():
    body = request.get_json()

    # get username from the http body
    username = body["username"]

    # open JSON file to log the user in
    with open('data/users.json', 'r') as file:
        # read the file as content
        content = json.load(file)

        # check if logged user is available in the saved data
        for user in content["users"]:
            if user["username"] == username:
                # return their current data
                return jsonify(user)
    
    # otherwise return 404
    return make_response(jsonify({'error': 'user not found'}), 404)

@app.route("/api/anime")
def getAnime():
    # open anime data
    with open('data/anime.json', 'r') as file:
        # read file as content
        content = json.load(file)

    return jsonify(content)

@app.route("/api/rate", methods=["POST"])
def rateAnime():
    body = request.get_json()

    # get username and anime ID from the http body
    username = body["username"]
    anime_name = body["anime_name"]
    anime_rating = body["anime_rating"]

    # open users data
    with open('data/users.json', 'r') as file:
        # read file as content
        content = json.load(file)

        for user in content["users"]:
            # set current anime rating for current user
            if user["username"] == username:
                # write to content
                user["rated"][anime_name] = anime_rating

                # update the file from updated content
                with open('data/users.json', 'w') as file:
                    json.dump(content, file)
            
                return jsonify(user)

    # otherwise return 404
    return make_response(jsonify({'error': 'data not found'}), 404)

@app.route("/api/recommendation", methods=["POST"])
def recommend():
    body = request.get_json()

    # get username from the http body
    username = body["username"]

    with open('data/users.json', 'r') as file:
        # read file as content
        content = json.load(file)

        for target in content["users"]:
            # set current anime rating for current user
            if target["username"] == username:
                recommendation = get_recommendation(target)

                # if no recommendation possible (score == 0)
                if recommendation == 0:
                    return jsonify({'error': 'no recommendation possible'})

                # return recommendation
                return jsonify({'data': recommendation})

    return make_response(jsonify({'error': 'user not found'}), 404)

@app.route("/api/history", methods=["POST"])
def history():
    body = request.get_json()

    # get username from the http body
    username = body["username"]

    with open('data/users.json', 'r') as file:
        # read file as content
        content = json.load(file)

        for target in content["users"]:
            # set current anime rating for current user
            if target["username"] == username:
                # Extract the real anime from anime.json
                with open('data/anime.json', 'r') as file:
                    animes = json.load(file)
                    result = []

                    for title in target["rated"]:
                        for anime in animes["animes"]:
                            if anime["title"] == title:
                                result.append(anime)
                                break

                    return result

    return make_response(jsonify({'error': 'user not found'}), 404)

