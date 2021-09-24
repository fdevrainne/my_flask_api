from numpy import int64
import pandas as pd
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from constant import END_POINT, DB_PATH

app = Flask(__name__)
api = Api(app)

arguments = reqparse.RequestParser()
arguments.add_argument("method", type=str, help="Name of the method is required", required=True)
arguments.add_argument("column", type=str, help="Name of the column is required", required=True)


class GetStats(Resource):
    def get(self):
        args = arguments.parse_args()
        method, column = args["method"], args["column"] 
        df = pd.read_csv(DB_PATH)
        if column not in df.columns:
            abort(404,message=f"The column {column} does not exist in the table")
        else:
            if method == "common":
                result = df[column].mode(dropna=False)[0]
                if isinstance(result, int64):
                    result = int(result)
            elif method == "values":
                result = len(df[column].unique())
            else:
                abort(404,message=f"The method {method} is not valid. The available methods are 'common' and 'values'")
        return {"result":result}


api.add_resource(GetStats, f"/{END_POINT}")

if __name__ == "__main__":
    app.run()
