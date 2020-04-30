from flask import request, Response
from flask_restful import Resource
import json
import database as db

class UserPatterns(Resource):
    # returns array of patterns owned by a user
    def get(self):
        try:
            userId = request.args.get("userId")
            query = "SELECT * FROM patterns WHERE userId = ? ORDER BY startDate DESC"
            params = [userId]
            res = db.Execute(query, params)
            if len(res) > 0:
                response = []
                for row in res:
                    temp = {
                        "userId": row[0],
                        "startDate": row[1],
                        "prices": row[2],
                        "first": bool(row[3]),
                        "pattern": row[4]
                    }
                    response.append(temp)

                return Response(json.dumps(response), status=200, mimetype="application/json")
            else:
                return Response("{ 'message' : 'No patterns found' }", status=404, mimetype="application/json")
        except:
            return Response(status=500)

class SubmitPattern(Resource):
    # creates/updates record for pattern
    def put(self):
        userId = request.json["userId"]
        startDate = request.json["startDate"]
        prices = request.json["prices"]
        first = int(request.json["first"])
        pattern = request.json["pattern"]
        query = "SELECT * FROM patterns WHERE userId = ? AND startDate = ?"
        params = [userId, startDate]
        res = db.Execute(query, params)

        if len(res) > 0:
            query = """
                UPDATE patterns SET
                    prices = ?,
                    first = ?,
                    pattern = ?
                WHERE userId = ? AND startDate = ?
            """
            params = [prices, first, pattern, userId, startDate]
            res = db.Execute(query, params, True)
            if res is None:
                return Response(status=500)
            else:
                return Response(status=200)
        else:
            query = """
                INSERT INTO patterns (userId, startDate, prices, first, pattern)
                VALUES (?, ?, ?, ?, ?)
            """
            params = [userId, startDate, prices, first, pattern]
            res = db.Execute(query, params, True)
            if res is None:
                return Response(status=500)
            else:
                return Response(status=200)