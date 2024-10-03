from flask import Flask
from flask_script import Server, Manager

app = Flask(__name__)
manager = Manager(app)
server = Server(host="0.0.0.0", port=80, threaded=True)
manager.add_command("runserver", server)

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    manager.run()