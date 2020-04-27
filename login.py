from flask import request, Response
from flask_restful import Resource

class Login(Resource):
    # logs the user in
    # for now we will just accept usernames. if we want to go bigger then
    # i'll start considering passwords
    def post(self):
        username = request.json["username"]
        # TODO: check if user exists in db, if they do log in if not reject login
        # we'll just pretend that only i can get in for now
        if username == "pondo":
            return Response(status=200)
        else:
            return Response(status=404)