import os
from flask import Flask, render_template, request, send_from_directory
import qrcode

app = Flask(__name__)

# Caminho para o diretório 'static'
STATIC_DIR = os.path.join(os.getcwd(), 'static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    qr = qrcode.make(data)
    # Caminho completo para salvar o arquivo 'qrcode.png' no diretório 'static'
    qr_path = os.path.join(STATIC_DIR, 'qrcode.png')
    qr.save(qr_path)
    return render_template('generate.html', qr_path=qr_path)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
