from flask import request, Response
from flask_restful import Resource
import json
import database as db

class Login(Resource):
    # logs the user in
    # for now we will just accept usernames. if we want to go bigger then
    # i'll start considering passwords
    def post(self):
        try:
            username = request.json["username"]
            query = "SELECT * FROM users WHERE username = ?"
            params = [username]
            res = db.Execute(query, params)
            if len(res) > 0:
                response = {
                    "message": "User authenticated",
                    "userData": {
                        "userId": res[0][0],
                        "username": res[0][1]
                    }
                }
                return Response(json.dumps(response), status=200, mimetype="application/json")
            else:
                return Response("{ 'message' : 'Failed to authenticate user' }", status=401, mimetype="application/json")
        except:
            return Response(status=500)