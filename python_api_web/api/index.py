from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# directorio raíz al path para importar app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# necesario para Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))