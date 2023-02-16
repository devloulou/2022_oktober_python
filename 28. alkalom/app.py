"""
Flask - ligthweigth webframework - modul
weboldalhoz tartozó backendet, RestAPI-kat tudunk csinálni
"""
from flask import Flask

app = Flask("test_app")

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/masik_route")
def masik():
    return "Hello world masik!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)