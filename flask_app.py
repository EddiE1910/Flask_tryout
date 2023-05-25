from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=500,debug=True)

@app.route('/')
def home():
    return "<p>Hello world!</p>"

@app.route('/test')
def test():
    return "Dit is een test"