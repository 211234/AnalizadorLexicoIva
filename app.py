# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Lista para almacenar productos
productos = []

# Función para calcular IVA y total
def calcular_iva(precio):
    iva = precio * 0.16
    total = precio + iva
    return precio, iva, total

@app.route('/', methods=['GET', 'POST'])
def index():
    global productos
    if request.method == 'POST':
        if 'borrar' in request.form:
            productos = []
        else:
            producto = request.form['producto']
            precio_str = request.form['precio']
            
            try:
                precio = float(precio_str)
            except ValueError:
                return "Precio inválido. Asegúrate de ingresar un número válido.", 400
            
            precio, iva, total = calcular_iva(precio)
            
            # Convertir a dos decimales
            precio = "{:.2f}".format(precio)
            iva = "{:.2f}".format(iva)
            total = "{:.2f}".format(total)
            
            productos.append({'producto': producto, 'precio': precio, 'iva': iva, 'total': total})
        
        return redirect(url_for('index'))
    
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
