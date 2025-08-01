from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'password123'
csrf = CSRFProtect(app)

@app.route('/')
def home():
    return "Aplikasi Manajemen Inventaris - TechNova"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
