from flask import Flask, render_template, request, jsonify
import os
import sys

# Include the cipher directory without needing __init__.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'cipher'))

import old_code
import improve_code

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_old', methods=['POST'])
def process_old():
    data = request.get_json()
    text = data.get('text', '')
    mode = data.get('mode', '')

    if mode == 'encrypt':
        result = old_code.encrypt(text)
    elif mode == 'decrypt':
        result = old_code.decrypt(text)
    else:
        result = "Invalid mode"

    return jsonify({'result': result})

@app.route('/process_improved', methods=['POST'])
def process_improved():
    data = request.get_json()
    text = data.get('text', '')
    mode = data.get('mode', '')

    rotation1 = improve_code.generate_collatz_key()
    keyset = improve_code.generate_rotations(rotation1, [1, 10])

    if mode == 'encrypt':
        result, _ = improve_code.encrypt_improved(text, keyset)
    elif mode == 'decrypt':
        result = improve_code.decrypt_improved(text, keyset)
    else:
        result = "Invalid mode"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
