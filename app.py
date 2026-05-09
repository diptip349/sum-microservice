from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum')
def sum_values():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"sum": a + b})

app.run(host='0.0.0.0', port=5000) 