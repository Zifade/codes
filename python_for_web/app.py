# let's import the flask

from flask import Flask, render_template, request, redirect, url_for
import re
from collections import Counter
import os

app = Flask(__name__)

@app.route('/')
def home(): 
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/result')
def result():
    if not hasattr(app, 'analysis_results'):
        return redirect(url_for('post'))
    
    # Obtener resultados
    results = app.analysis_results
    return render_template('result.html', results=results, title='Analysis Results')

@app.route('/post', methods=['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        
        results = analyze_text(content)

        app.analysis_results = results
        
        return redirect(url_for('result'))

def analyze_text(text):
    """
    Analiza el texto para contar palabras, caracteres y palabras más frecuentes.
    """
    # limpiar texto
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # dividir
    words = re.findall(r'\b\w+\b', cleaned_text)
    
    # contar palabras
    word_count = len(words)
    
    # contar caracteres
    char_count = len(text)
    
    # contar caracteres (sin espacio)
    char_count_no_spaces = len(text.replace(' ', ''))
    
    # palabras más frecuentes
    stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'but', 'is', 'are', 'was', 'were','that','this','it'}
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1]
    word_freq = Counter(filtered_words).most_common(10)  # Top 10 palabras más frecuentes
    
    # Preparar resultados
    results = {
        'original_text': text,
        'word_count': word_count,
        'char_count': char_count,
        'char_count_no_spaces': char_count_no_spaces,
        'word_freq': word_freq
    }
    
    return results

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)