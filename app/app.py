import os

from flask import Flask, jsonify, render_template, request
import sqlite3

from app.query import generate_filter_query

app = Flask(__name__)
database_path = os.path.join(app.root_path, 'db/main.db')
@app.route('/')
def home():
    print("Home page")
    print(app.root_path)
    return render_template('index.html')

@app.route('/generate_json', methods=['GET'])
def generate_json():
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)  # Replace 'your_database.db' with your actual database file name
    cursor = conn.cursor()

    filters = {}
    filters['age'] = request.args.get('age')
    filters['age_comparison'] = request.args.get('age_comparison')
    filters['place'] = request.args.get('place')
    filters['mainNoise'] = request.args.get('main_noise')
    filters['frequency_in_noisy_place'] = request.args.get('frequency')
    filters['frequency_comparison'] = request.args.get('frequency_comparison')
    filters['noise_rating'] = request.args.get('noise_rating')
    filters['noise_impact_rating'] = request.args.get('noise_impact_rating')
    filters['illness_from_noise'] = request.args.get('illness')
    filters['sleep_problem'] = request.args.get('sleep_problem')
    filters['noise_control_measures'] = request.args.get('noise_control')

    query, values, key_sort = generate_filter_query(filters)

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

