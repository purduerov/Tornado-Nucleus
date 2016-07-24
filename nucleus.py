import time
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
sum = 0.0
total = 0.0
lt = time.time()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('status')
def status(data):
    now = time.time()
    global sum
    global total
    global lt

    sum += (now - lt)
    total += 1.0
    print (now - lt) * 1000.0, (sum / total) * 1000.0
    lt = now
    socketio.emit('status', {'data': 'got it!'})

socketio.run(app)
