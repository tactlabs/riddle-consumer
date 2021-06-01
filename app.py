from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


"""
http://0.0.0.0:8080/consumer

"""

@app.route('/')
def api_riddle():

    

    pass

if __name__ == "__main__":
    app.run( debug = True, host="0.0.0.0", port = 3005)