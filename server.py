from flask import Flask, json, jsonify, make_response, render_template, request

app = Flask(__name__)

@app.route("/")
def indexPage():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    return render_template("login.html")

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
