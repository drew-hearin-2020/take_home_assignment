from flask import Flask, jsonify
from json import JSONEncoder
import datetime, json

app = Flask(__name__)

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

@app.route("/")
def getDate():
    current_date = { "Current DateTime ": datetime.datetime.now() }
    currentJSONData = json.dumps(current_date, cls=DateTimeEncoder)
    return currentJSONData

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')