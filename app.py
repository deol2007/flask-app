from flask import Flask, jsonify, request
from numpy import array
from requests import JSONDecodeError

app=Flask(__name__)

{
    "data": [
        {
            'Contact':999263892,
            'Name':'Mother',
            'done': False,
            'id': 1
        },
        {
            'Contact':438924717,
            'Name':'Father',
            'done': False
            'id':2,
        }
    ]
}


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message":"please provide data"
        },400)
    data={
        'Contact':request.json['Contact'],
        'Name':request.json.get('Name',""),
        'done': False,
        'id':data[-1]['id']+1
    }
    data.append(data)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": data
    })
if (__name__ == "__main__"):
    app.run(debug=True)