from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    image = Image.open(file)
    image_path = 'uploads/original.png'
    image.save(image_path)

    return render_template('index.html', image_path=image_path)

@app.route('/encrypt/<key>')
def encrypt(key):
    image_path = 'uploads/original.png'
    encrypted_path = 'uploads/encrypted.png'
    encrypt_image(image_path, int(key), encrypted_path)
    return render_template('index.html', encrypted_path=encrypted_path)

@app.route('/decrypt/<key>')
def decrypt(key):
    encrypted_path = 'uploads/encrypted.png'
    decrypted_path = 'uploads/decrypted.png'
    decrypt_image(encrypted_path, int(key), decrypted_path)
    return render_template('index.html', decrypted_path=decrypted_path)

def encrypt_image(image_path, key, encrypted_path):
    original_image = Image.open(image_path)
    image_array = np.array(original_image)
    encrypted_image_array = image_array + key
    encrypted_image = Image.fromarray(encrypted_image_array.astype('uint8'))
    encrypted_image.save(encrypted_path)

def decrypt_image(encrypted_image_path, key, decrypted_path):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_array = np.array(encrypted_image)
    decrypted_image_array = encrypted_image_array - key
    decrypted_image = Image.fromarray(decrypted_image_array.astype('uint8'))
    decrypted_image.save(decrypted_path)


if __name__ == '__main__':
    app.run(debug=True)
