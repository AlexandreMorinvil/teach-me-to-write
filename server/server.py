import logging
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from flask import jsonify
from flask.wrappers import Response


# Server initializations
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
ssid = None

# Deactivate socket.io logs
logging.getLogger('socketio').setLevel(logging.ERROR)
logging.getLogger('engineio').setLevel(logging.ERROR)
# logging.getLogger('werkzeug').setLevel(logging.ERROR)

# Server connections global variables
connections_set = set()

####################################################################################################
#### Handling the socket connections.
####################################################################################################
@socketio.on('connect')
def handle_connection():
    connections_set.add(request.sid)
    print("New User {request.sid} connected.  Current users :", connections_set)

####################################################################################################
#### Handling the socket disconnections.
####################################################################################################
@socketio.on('disconnect')
def handle_disconnection():
    connections_set.discard(request.sid)
    print("User disconnected. Current users : ", connections_set)

####################################################################################################
#### Reception and handling of commands from the tablet.
####################################################################################################
@app.route("/command", methods=["POST", "GET"])
def command() -> Response:
    command = request.get_json()
    response = None
    print("Received a request")
    return jsonify({"content": response})

####################################################################################################
#### Launching the server
####################################################################################################
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
