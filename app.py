from flask import Flask, jsonify, make_response, redirect
from netflix import db, routes


app = Flask(__name__)

app.register_blueprint(routes.netflix_api, url_prefix='/netflix')


@app.route("/")
def hello_from_root():
    return jsonify(message='Welcome to my DB, enter /netflix in the URL to see the movies data !')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
