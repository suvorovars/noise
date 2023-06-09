import os

from flask import Flask, jsonify, render_template, request
import sqlite3

from app.query import generate_filter_query

app = Flask(__name__)
database_path = os.path.join(app.root_path, 'db/main.db')

@app.route('/')
def index():
    db = sqlite3.connect(database_path, check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, sender_name TEXT, caption TEXT)')
    db.commit()
    cursor.execute('SELECT * FROM images')
    images = cursor.fetchall()
    return render_template('index.html', images=images)
@app.route('/api')
def api_page():
    return render_template('api.html')

@app.route('/api/upload', methods=['POST'])
def upload():
    db = sqlite3.connect(database_path, check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, sender_name TEXT, caption TEXT)')
    db.commit()

    print(request.view_args)
    file = request.files['file']
    sender_name = request.form['sender_name']
    caption = request.form['caption']

    if file:
        filename = file.filename
        file.save('app/static/uploaded_images/' + filename)

        cursor.execute('INSERT INTO images (filename, sender_name, caption) VALUES (?, ?, ?)',
                       (filename, sender_name, caption))
        db.commit()

        return 'File uploaded successfully!'
    else:
        return 'No file uploaded!'

@app.route('/api/generate_survey', methods=['GET'])
def generate_survey():
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    filters = {}
    filters['age'] = request.args.get('age')
    filters['age_comparison'] = request.args.get('age_comparison')
    filters['place'] = request.args.get('place')
    filters['mainNoise'] = request.args.get('main_noise')
    filters['frequency_in_noisy_place'] = request.args.get('frequency')
    filters['frequency_in_noisy_place_comparison'] = request.args.get('frequency_comparison')
    filters['noise_rating'] = request.args.get('noise_rating')
    filters['noise_rating_comparison'] = request.args.get('noise_rating_comparison')
    filters['noise_impact_rating'] = request.args.get('noise_impact_rating')
    filters['noise_impact_rating_comparison'] = request.args.get('noise_impact_rating_comparison')
    filters['illness_from_noise'] = request.args.get('illness')
    filters['sleep_problem'] = request.args.get('sleep_problem')
    filters['noise_control_measures'] = request.args.get('noise_control')
    filters['sort_key'] = request.args.get('sort_key')


    query, values = generate_filter_query(filters)

    cursor.execute(query, tuple(values))

    rows = cursor.fetchall()

    # Prepare the data as a list of dictionaries
    data = []
    for row in rows:
        survey_dict = {
            'id': row[0],
            'age': row[1],
            'place': row[2],
            'mainNoise': row[3],
            'frequency_in_noisy_place': row[4],
            'noise_rating': row[5],
            'noise_impact_rating': row[6],
            'illness_from_noise': row[7],
            'sleep_problem': row[8],
            'noise_control_measures': row[9]
        }
        data.append(survey_dict)

    # Close the database connection
    conn.close()

    # Create and send the JSON response
    response = jsonify(data)
    response.headers['Content-Disposition'] = 'attachment; filename=survey_data.json'
    return response

