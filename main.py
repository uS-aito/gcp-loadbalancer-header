from flask import Flask, request
import os
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    with open("./header.log", "a") as f:
        f.write(str(request.headers)+os.linesep)

    return "Hello, World!"

class Writer(object):
    def __init__(self, filename):
        self.file = open(filename, "a")
    
    def write(self,data):
        self.file.write(data)
    
    def flush(self, data):
        self.file.flush()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: %s port" % (sys.argv[0]))
    
    p = int(sys.argv[1])
    app.run(host="0.0.0.0", port=p, debug=True)