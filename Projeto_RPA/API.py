from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
with open(BASE_DIR + '\\Projeto_RPA\\notebooks.json') as f:    
    notebooks = json.load(f)

@app.route('/notebooks', methods=['GET'])
def home():
    return jsonify(notebooks), 200

@app.route('/notebooks/<string:Nome>', methods=['GET'])
def notebooks_per_Nome(Nome):
    notebooks_per_Nome = [notebook for notebook in notebooks if Nome in notebook['Nome']]
    return jsonify(notebooks_per_Nome), 200

if __name__ == '__main__':
    app.run(debug=True)