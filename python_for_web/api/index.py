from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Añadir el directorio raíz al path para poder importar app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar la app desde tu archivo app.py original
from app import app

# Esto es necesario para Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))