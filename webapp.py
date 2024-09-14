from flask import Flask , render_template 
import mysql.connector 
import os 
app = Flask(__name__, template_folder='.')


db_config = {
    'user': os.environ['DBUSER'],
    'password': os.environ['DBPASSWORD'],
    'host': os.environ['DBHOST'],
    'database': os.environ['DB'], 
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients')
def clients():
    conn = mysql.connector.connect(**db_config)
    conn.set_charset_collation('utf8mb4', 'utf8mb4_unicode_ci')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM client")
    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]

    cursor.close()
    conn.close()

    return render_template('clients.html', rows=rows, column_names=column_names)
     
@app.route('/register')
def register(): 
    return "Under construction"

if __name__ == "__main__": 
    app.run() 
    