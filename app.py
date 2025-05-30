from flask import Flask, render_template
import threading
import time
import random

app = Frasco(__name__)

logs = []

def robo_operando():
    while True:
        time.sleep(2)
        score = round(random.uniform(90, 100), 2)
        entrada = random.choice(["BUY", "SELL"])
        resultado = random.choice(["WIN", "LOSS"])
        logs.append(f"[{time.strftime('%H:%M:%S')}] Score: {score} | Entrada: {entrada} | Resultado: {resultado}")
        if len(logs) > 50:
            logs.pop(0)

@app.route('/')
def index():
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    t = threading.Thread(target=robo_operando)
    t.daemon = True
    t.start()
    app.run(debug=True, host='0.0.0.0', port=10000)
