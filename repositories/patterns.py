from flask import request, Response
from flask_restful import Resource
import json

class UserPatterns(Resource):
    # returns array of patterns owned by a user
    def get(self):
        # TODO: actually get the user's patterns
        id = int(request.args.get("userId"))
        if id == 1:
            res = [
                {
                    "startDate": 1587945600,
                    "prices": "100.121.113..........",
                    "first": False,
                    "pattern": 0
                }
            ]
            return Response(json.dumps(res), status=200, mimetype="application/json")
        else:
            return Response("{ 'message' : 'No patterns found' }", status=404, mimetype="application/json")

class SubmitPattern(Resource):
    def put(self):
        # TODO: create new/update record
        id = request.json["userId"]
        patternObj = request.json["pattern"]
        return Response("{ 'message' : 'method unimplemented' }", status=501, mimetype="application/json")