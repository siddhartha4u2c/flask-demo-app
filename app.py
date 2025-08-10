from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! 🌍 This is a new simple Flask app.'

if __name__ == '__main__':
    app.run(debug=True)

"""deployed at https://flask-demo-app-3.onrender.com/"""
