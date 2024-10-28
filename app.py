from flask import Flask, render_template, request, jsonify
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.get_json()  # Récupérer les données JSON envoyées par le client
    link = data['link']
    color = data['color']  # Récupérer la couleur

    # Créer un QR code avec fond transparent
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Créer une image avec un fond transparent
    img = qr.make_image(fill_color=color, back_color="transparent")  # Utiliser la couleur choisie

    # Convertir le QR code en image base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    qr_img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({'qr_code': qr_img_str})

if __name__ == '__main__':
    app.run(debug=True)
