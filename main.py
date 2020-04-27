from flask import Flask, request
from flask_restful import Resource, Api

# import repositories
from login import Login
from users import GetAllUsers, GetUser

app = Flask(__name__)
api = Api(app)

# define api paths
api.add_resource(Login, "/Login")
api.add_resource(GetAllUsers, "/GetAllUsers")
api.add_resource(GetUser, "/GetUser")

if __name__ == "__main__":
    app.run(debug=True)