from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=500,debug=True)

@app.route('/')
def home():
    return "<p>Dit zou eigenlijk in de template map moeten staan als .html bestand</p>"
