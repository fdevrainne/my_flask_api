from numpy import int64
import pandas as pd
from flask import Flask
from flask_restful import Api, Resource, abort

from constant import END_POINT, DB_PATH

app = Flask(__name__)
api = Api(app)

class GetStats(Resource):
    def get(self, method, column):
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


endpoint_params = f"/{END_POINT}/<string:method>/<string:column>"
api.add_resource(GetStats, endpoint_params)

if __name__ == "__main__":
    app.run()

