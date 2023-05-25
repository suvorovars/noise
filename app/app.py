import os

from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)
database_path = os.path.join(app.root_path, 'db/main.db')  # Замените 'your_database.db' на фактическое имя файла базы данных
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

    # Retrieve data from the 'survey' table
    cursor.execute("SELECT * FROM survey")
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

