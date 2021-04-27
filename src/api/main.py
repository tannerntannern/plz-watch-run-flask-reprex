from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'helloo', 200

app.run(port=8000)
