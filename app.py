from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>🚀 JARVIS FERA SOLTA está rodando com sucesso!</h1>"
