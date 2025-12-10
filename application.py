from flask import Flask, jsonify
import random
# ... (código completo del generador de paletas) ...
application = Flask(__name__) 

def generate_hex_color():
    """Genera un código de color hexadecimal aleatorio."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

@application.route('/')
def index():
    """Ruta principal."""
    instructions = {
        "Bienvenido": "Generador de Paletas de Colores Aleatorias (ECR Deployment)",
        "Uso": "Accede a la ruta /api/generate/<cantidad> para generar paletas.",
        "Ejemplo": "/api/generate/5 generará 5 colores."
    }
    return jsonify(instructions)

@application.route('/api/generate/<int:count>')
def generate_palette(count):
    # ... (lógica de generación de paletas) ...
    if count < 1 or count > 10:
        return jsonify({"error": "La cantidad debe ser entre 1 y 10."}), 400

    palette = [generate_hex_color() for _ in range(count)]
    
    response = {
        "paleta_generada": palette,
        "cantidad": count,
        "generado_por": "Flask Docker Microservice"
    }
    
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)