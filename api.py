#!flask/bin/python
from flask import Flask, jsonify, abort
from main import morphNorm

app = Flask(__name__)


@app.route('/morph/api/v1.0/norm/<string:text>', methods=['GET'])
def norm(text, dictSource='dictBase.csv', indexSource='index.csv'):
    return jsonify({'normalizedText': morphNorm(text.encode('UTF-8'), dictSource, indexSource)})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)