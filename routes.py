import pandas as pd
from flask import request, jsonify, Blueprint, Response
import queries

# sample user route
def construct_user_routes(db_conn):  # type: ignore
    user_routes = Blueprint("user_routes", __name__)

    @user_routes.route("/users", methods=['GET'])
    def get_users():
      try:
        data_f = pd.read_sql(
                      queries.get_all_users(), con=db_conn
                  )
        results = data_f.to_json(orient="records")
        return Response(results, 200)
      except ValueError as e:
        print(e)
    return user_routes