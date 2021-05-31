from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)


"""
http://0.0.0.0:8080/consumer

"""

@app.route('/consumer')
def api_riddle():

    name = request.get("url")

    
    return 

if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = 3005)