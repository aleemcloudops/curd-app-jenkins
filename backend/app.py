from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.json'

# Initialize data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(read_data())

@app.route('/notes', methods=['POST'])
def create_note():
    data = read_data()
    new_note = request.json
    new_note['id'] = len(data) + 1
    data.append(new_note)
    write_data(data)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = read_data()
    for note in data:
        if note['id'] == note_id:
            note.update(request.json)
            write_data(data)
            return jsonify(note)
    return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    data = read_data()
    data = [note for note in data if note['id'] != note_id]
    write_data(data)
    return jsonify({'message': 'Deleted'}), 200

# Optional health check route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
