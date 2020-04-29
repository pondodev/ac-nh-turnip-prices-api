from flask import Flask, request
from flask_restful import Resource, Api
import database as db

# import repositories
from repositories.login import Login
from repositories.users import AllUsers, User
from repositories.patterns import UserPatterns, SubmitPattern

app = Flask(__name__)
api = Api(app)

# define api paths
api.add_resource(Login, "/api/Login")
api.add_resource(AllUsers, "/api/AllUsers")
api.add_resource(User, "/api/User")
api.add_resource(UserPatterns, "/api/UserPatterns")
api.add_resource(SubmitPattern, "/api/SubmitPattern")

if __name__ == "__main__":
    db.Init()
    app.run(debug=True)