from flask import Flask, jsonify
from json import JSONEncoder
import datetime, json

app = Flask(__name__)

@app.route("/")
def getDate():
    class DateTimeEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    current_date = { "Current DateTime ": datetime.datetime.now() }
    currentJSONData = json.dumps(current_date, cls=DateTimeEncoder)
    return currentJSONData

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')