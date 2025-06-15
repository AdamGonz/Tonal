from flask import Flask, request, jsonify
from aztecDateConverter import convert_to_aztec

app = Flask(__name__)

@app.route('/aztec-date', methods=['GET'])
def aztec_date():
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({"error": "Missing 'date' parameter"}), 400

    try:
        result = convert_to_aztec(date_str)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
