# let's import the flask

from flask import Flask, render_template, request, Response, redirect, url_for
import re
from collections import Counter
import os # importing operating system module
import pymongo
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
MONGODB_URI = 'mongodb+srv://jorgelutz1:XHIz5HzUCo1cXJ7t@30daysofpython.e9nc9fv.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
# Creating database
db = client.thirty_days_of_python


app = Flask(__name__)

#-- home page

@app.route('/')
def home(): 
    back_techs = ['Python','Flask','MongoDB']
    front_techs= ['HTML', 'CSS', 'JavaScript']
    name = '30 Days Of Python Programming'
    return render_template('home.html', back_techs=back_techs, front_techs=front_techs, name=name, title='Home')

#-- about page

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

#-- page de resultados del analisis de texto

@app.route('/result')
def result():
    if not hasattr(app, 'analysis_results'):
        return redirect(url_for('post'))
    
    # Obtener resultados
    results = app.analysis_results
    return render_template('result.html', results=results, title='Analysis Results')

#-- text analizer page

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

#-- text analyzer backend logic

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

#-- manage students

@app.route('/manage-students')
def home ():
    name='Students'
    return render_template('manage_students.html', name=name, title='Students')

#-- api estudiantes --

#-- obtener estudiantes

@app.route('/api/v1.0/students', methods=['GET'])
def students():
    students_data = list(db.students.find({}))
    
    return Response(dumps(students_data), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find_one({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

#-- crear estudiantes

@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        # Obtener datos formulario
        name = request.form.get('name')
        country = request.form.get('country')
        city = request.form.get('city')
        skills_str = request.form.get('skills', '')
        skills = [skill.strip() for skill in skills_str.split(',')] if skills_str else []
        bio = request.form.get('bio', '')
        birthyear = request.form.get('birthyear')
        
        if not name or not country or not city:
            return Response(
                dumps({"error": "Name, country and city are required"}),
                status=400,
                mimetype='application/json'
            )
        
        # Crear documento
        student = {
            'name': name,
            'country': country,
            'city': city,
            'birthyear': birthyear,
            'skills': skills,
            'bio': bio,
            'created_at': datetime.now()
        }
        
        # Insertar en bd
        result = db.students.insert_one(student)
        # retornar estudiante
        created_student = db.students.find_one({'_id': result.inserted_id})
        
        return Response(
            dumps(created_student),
            status=201,
            mimetype='application/json'
        )
    
    except Exception as e:
        return Response(
            dumps({"error": str(e)}),
            status=500,
            mimetype='application/json'
        )
    
# --Actualizar estudiante

@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        query = {"_id": ObjectId(id)}
        
        # Verificar existencia
        if not db.students.find_one(query):
            return Response(dumps({"error": "Student not found"}), status=404, mimetype='application/json')
        
        # Obtener datos del formulario
        name = request.form.get('name')
        country = request.form.get('country')
        city = request.form.get('city')
        skills_str = request.form.get('skills', '')
        skills = [skill.strip() for skill in skills_str.split(',')] if skills_str else []
        bio = request.form.get('bio', '')
        birthyear = request.form.get('birthyear')
        
        # Crear documento con los campos a actualizar
        student = {
            'name': name,
            'country': country,
            'city': city,
            'birthyear': birthyear,
            'skills': skills,
            'bio': bio,
            'updated_at': datetime.now()
        }
        
        # Actualizar en bd
        db.students.update_one(query, {'$set': student})
        
        # Obtener y devolver documento actualizado
        updated_student = db.students.find_one(query)
        return Response(dumps(updated_student), mimetype='application/json')
    
    except Exception as e:
        return Response(dumps({"error": str(e)}), status=500, mimetype='application/json')
    
#-- borrar estudiante

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        query = {"_id": ObjectId(id)}
        
        # Verificar existencia
        student = db.students.find_one(query)
        if not student:
            return Response(
                dumps({"error": "Student not found"}),
                status=404,
                mimetype='application/json'
            )
        result = db.students.delete_one(query)
        
        # Verificar eliminación
        if result.deleted_count == 1:
            return Response(
                dumps({"message": "Student deleted successfully"}),
                status=200,
                mimetype='application/json'
            )
        else:
            return Response(
                dumps({"error": "Failed to delete student"}),
                status=500,
                mimetype='application/json'
            )
    
    except Exception as e:
        return Response(
            dumps({"error": str(e)}),
            status=500,
            mimetype='application/json'
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)