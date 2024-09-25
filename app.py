from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Ruta para la página inicial, donde se ingresa el peso
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el peso y mostrar la imagen con música
@app.route('/procesar', methods=['POST'])
def procesar():
    peso = request.form['peso']  # Captura el peso del formulario
    return render_template('imagen.html', peso=peso)

# Ruta para la imagen (en la misma carpeta)
@app.route('/imagen')
def imagen():
    return send_file('obesa.jpg', mimetype='image/jpg')

# Ruta para la música (en la misma carpeta)
@app.route('/musica')
def musica():
    return send_file('cancion.mp3', mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

