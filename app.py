from flask import Flask
import os
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Simple Test Server!</h3>" \
           "<b>Server Time:</b> {time}<br/>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(time=datetime.datetime.now(), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
