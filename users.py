from flask import request, Response
from flask_restful import Resource
import json

class GetAllUsers(Resource):
    # returns array of user uuids and names
    def get(self):
        # TODO: get all of the user uuids and names
        res = [{ "id" : 1, "username" : "pondo"}]
        return Response(json.dumps(res), status=200, mimetype="application/json")

class GetUser(Resource):
    # returns related user information
    def get(self):
        # TODO: get user information
        # for now we'll only return stuff if id == 1
        id = int(request.args.get("id"))
        if id == 1:
            res = { "id" : 1, "username" : "pondo"}
            return Response(json.dumps(res), status=200, mimetype="application/json")
        else:
            return Response(status=404)