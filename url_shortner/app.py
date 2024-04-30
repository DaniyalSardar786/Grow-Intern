from flask import Flask, render_template, request, redirect
import shortuuid
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'url_shortener.db'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = shortuuid.uuid()[:8]  # Generate short URL
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
        conn.commit()
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    if result:
        original_url = result[0]
        return redirect(original_url)
    else:
        return 'URL not found'

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
