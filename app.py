from flask import Flask, request, jsonify
import dividend_eng as de

app = Flask(__name__)

@app.route('/list', methods=['POST'])
def list():
    watchlist = request.json['watchlist']
    result = {}
    for symbol in watchlist:
        data = de.Stock(symbol)
        result.update({symbol : data.get_data()})    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)