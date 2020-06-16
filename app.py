from flask import Flask, request, jsonify
from flask_cors import CORS
import dividend_eng as de

app = Flask(__name__)
CORS(app)

@app.route('/list', methods=['POST'])
def list():
    watchlist = request.json['watchlist']
    result = {}
    #? Modificare per multithread??
    for symbol in watchlist:
        data = de.Stock(symbol)
        result.update({symbol : data.get_data()})    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)