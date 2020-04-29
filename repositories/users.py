import sys
from flask import request, Response
from flask_restful import Resource
import json
import secrets
import database as db

class AllUsers(Resource):
    # returns array of user uuids and names
    def get(self):
        try:
            query = "SELECT * FROM users"
            res = db.Execute(query)
            response = []
            for row in res:
                temp = {
                    "userId": row[0],
                    "username": row[1]
                }
                response.append(temp)

            return Response(json.dumps(response), status=200, mimetype="application/json")
        except:
            return Response(status=500)

class User(Resource):
    # returns related user information
    def get(self):
        try:
            userId = int(request.args.get("userId"))
            query = "SELECT * FROM users WHERE userId = " + str(userId)
            res = db.Execute(query)
            if len(res) == 0:
                return Response(status=404)
            else:
                response = {
                    "userId" : res[0][0],
                    "username" : res[0][1]
                }
                return Response(json.dumps(response), status=200, mimetype="application/json")
        except:
            return Response(status=500)

    # creates a user account
    # for now we will only accept usernames, passwords can come later
    # if this becomes a bigger thing
    def post(self):
        # get randomly generated user id
        userId = -1
        # loop until id is unique
        while userId == -1:
            userId = secrets.randbelow(9999999)
            query = "SELECT * FROM users WHERE userId = " + str(userId)
            res = db.Execute(query)
            if len(res) > 0:
                userId = -1

        username = request.json["username"]
        try:
            query = "INSERT INTO users (userId, username) VALUES (" + str(userId) + ", '" + username + "')"
            res = db.Execute(query, True)
            if res is None:
                return Response(status=500)
            else:
                response = {
                    "userId": userId,
                    "username": username
                }
                return Response(json.dumps(response), status=200, mimetype="application/json")
        except:
            return Response(status=500)