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

    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]

    cursor.close()
    conn.close()

    return render_template('clients.html', rows=rows, column_names=column_names)
     
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            lastname = request.form['lastname']

            conn = mysql.connector.connect(**db_config)
            conn.set_charset_collation('utf8mb4', 'utf8mb4_unicode_ci')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO clients (name, lastname) VALUES (%s, %s)", (name, lastname))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('clients'))
        except Exception as e:
            return f"Error: {e}"  # temporary debugging
    return render_template('register.html')



if __name__ == "__main__": 
    app.run() 
    
