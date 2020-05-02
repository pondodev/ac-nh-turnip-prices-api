from flask import Flask, request
from flask_restful import Resource, Api
import database as db

# import repositories
from repositories.login import Login
from repositories.users import AllUsers, User
from repositories.patterns import UserPatterns, SubmitPattern

app = Flask(__name__, static_url_path="", static_folder="./site")
api = Api(app)

# paths for the static site
@app.route("/")
def rootPage():
    return app.send_static_file("index.html")
@app.route("/login")
def loginPage():
    return app.send_static_file("login.html")

# define api paths
api.add_resource(Login, "/api/Login")
api.add_resource(AllUsers, "/api/AllUsers")
api.add_resource(User, "/api/User")
api.add_resource(UserPatterns, "/api/UserPatterns")
api.add_resource(SubmitPattern, "/api/SubmitPattern")

if __name__ == "__main__":
    db.Init()
    app.run(debug=True, port=80)