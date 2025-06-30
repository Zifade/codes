# let's import the flask
from flask import Flask, render_template, request, Response, redirect, url_for
from flask import request, jsonify
import re
from collections import Counter
import os # importing operating system module
import pymongo
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
import certifi
import time  # ← AÑADIR ESTA IMPORTACIÓN

app = Flask(__name__)

# Optimización para serverless - conexión lazy
_client = None
_db = None

# ← AÑADIR ESTAS VARIABLES PARA EL CACHÉ
_cache = {}
_cache_time = {}
CACHE_DURATION = 60  # 1 minuto

def get_db():
    global _client, _db
    if _client is None:
        MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb+srv://jorgelutz1:XHIz5HzUCo1cXJ7t@30daysofpython.e9nc9fv.mongodb.net/thirty_days_of_python')
        
        # Conexión ultra-rápida
        _client = pymongo.MongoClient(
            MONGODB_URI,
            serverSelectionTimeoutMS=3000,  # 3 segundos máximo
            connectTimeoutMS=3000,
            socketTimeoutMS=3000,
            maxPoolSize=1,
            minPoolSize=0,
            maxIdleTimeMS=30000
        )
        _db = _client.thirty_days_of_python
    return _db

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

#-- manage students ← AQUÍ IMPLEMENTAR CACHÉ
@app.route('/manage-student')
def manage_student(): 
    try:
        # Verificar caché
        if 'manage_students' in _cache and time.time() - _cache_time.get('manage_students', 0) < CACHE_DURATION:
            return render_template('manage_student.html', students=_cache['manage_students'])
        
        # Si no hay caché, consultar BD
        db = get_db()
        students_data = list(db.students.find({}).limit(20))  # Reducir a 20
        
        # Guardar en caché
        _cache['manage_students'] = students_data
        _cache_time['manage_students'] = time.time()
        
        return render_template('manage_student.html', students=students_data)
    except Exception as e:
        return f"Error connecting to database: {str(e)}", 500

#-- add students
@app.route('/add-student')
def add_student(): 
    return render_template('add_student.html')

#-- api estudiantes --

#-- obtener estudiantes ← AQUÍ IMPLEMENTAR CACHÉ
@app.route('/api/v1.0/students', methods=['GET'])
def students():
    try:
        # Verificar caché
        if 'students' in _cache and time.time() - _cache_time.get('students', 0) < CACHE_DURATION:
            return Response(dumps(_cache['students']), mimetype='application/json')
        
        # Si no hay caché, consultar BD
        db = get_db()
        students_data = list(db.students.find({}).limit(20))  # Reducir a 20
        
        # Guardar en caché
        _cache['students'] = students_data
        _cache_time['students'] = time.time()
        
        return Response(dumps(students_data), mimetype='application/json')
    except Exception as e:
        return Response(
            dumps({"error": f"Database connection failed: {str(e)}"}),
            status=500,
            mimetype='application/json'
        )

@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    try:
        # Verificar caché individual
        cache_key = f'student_{id}'
        if cache_key in _cache and time.time() - _cache_time.get(cache_key, 0) < CACHE_DURATION:
            return Response(dumps(_cache[cache_key]), mimetype='application/json')
        
        db = get_db()
        student = db.students.find_one({'_id': ObjectId(id)})
        if not student:
            return Response(dumps({"error": "Student not found"}), status=404, mimetype='application/json')
        
        # Guardar en caché
        _cache[cache_key] = student
        _cache_time[cache_key] = time.time()
        
        return Response(dumps(student), mimetype='application/json')
    except Exception as e:
        return Response(
            dumps({"error": str(e)}),
            status=500,
            mimetype='application/json'
        )

#-- crear estudiantes ← LIMPIAR CACHÉ CUANDO SE CREA
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        db = get_db()
        
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
        
        # ← LIMPIAR CACHÉ DESPUÉS DE CREAR
        if 'students' in _cache:
            del _cache['students']
        if 'manage_students' in _cache:
            del _cache['manage_students']
        
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

# --Actualizar estudiante ← LIMPIAR CACHÉ CUANDO SE ACTUALIZA
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        db = get_db()
        obj_id = ObjectId(id)
        
        # Obtener los datos del formulario
        name = request.form.get('name')
        country = request.form.get('country')
        city = request.form.get('city')
        skills = request.form.get('skills', '').split(',')
        birthyear = request.form.get('birthyear')
        bio = request.form.get('bio')

        update_data = {
            "name": name,
            "country": country,
            "city": city,
            "skills": [s.strip() for s in skills],
            "birthyear": int(birthyear) if birthyear else None,
            "bio": bio
        }

        result = db.students.update_one({"_id": obj_id}, {"$set": update_data})

        if result.matched_count == 0:
            return jsonify({"error": "Student not found"}), 404

        # ← LIMPIAR CACHÉ DESPUÉS DE ACTUALIZAR
        cache_keys_to_remove = [key for key in _cache.keys() if key.startswith('student_') or key in ['students', 'manage_students']]
        for key in cache_keys_to_remove:
            if key in _cache:
                del _cache[key]

        return jsonify({"message": "Student updated successfully"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#-- borrar estudiante ← LIMPIAR CACHÉ CUANDO SE BORRA
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        db = get_db()
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
            # ← LIMPIAR CACHÉ DESPUÉS DE BORRAR
            cache_keys_to_remove = [key for key in _cache.keys() if key.startswith('student_') or key in ['students', 'manage_students']]
            for key in cache_keys_to_remove:
                if key in _cache:
                    del _cache[key]
            
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