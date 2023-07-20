from flask import Flask, request, jsonify
import model

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Server is running'

#get the json data
@app.route('/get_sentiment', methods = ['POST'])
def get_sentiment():
    tx = request.get_json(force = True)
    text = tx['Review']
    sent=model.get_predictor(text)
    return jsonify(result = sent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader = False)