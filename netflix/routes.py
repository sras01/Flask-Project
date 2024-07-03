from flask import Blueprint, json
from flask import flash
from flask import g
from flask import redirect
from flask import jsonify
from flask import request, render_template
from flask import url_for
from bson import ObjectId, json_util
from netflix.db import get_db

netflix_api = Blueprint("netflix", "netflix_api")

db = get_db()


@netflix_api.route("/", methods=["GET"])   # Fetches the entire data in the db
def fetch_all_movies():
    movies = []
    for movie in db['movies'].find({}):
        movies.append(movie)

    movies = json.loads(json_util.dumps(movies))

    return jsonify(movies=movies)


@netflix_api.route("/", methods=["POST"])    # Create / Insert new collection in to the data 
def insert_movie():
    data = request.get_json()

    req_body = {
        "age_certification": data['age_certification'],
        "description": data['description'],
        "genres": data['genres'],
        "id": data['id'],
        "imdb_score": data['imdb_score'],
        "production_countries": data['production_countries'],
        "release_year": data['release_year'],
        "runtime": data['runtime'],
        "title": data['title'],
        "type": data['type']
    }

    res = {}

    result = db['movies'].insert_one(req_body)

    res['id'] = json.loads(json_util.dumps(result.inserted_id))

    return jsonify(data=res)


@netflix_api.route("/<string:id>", methods=["GET"])   #  Fetch the data based on the provided title
def fetch_movie(id):
    if "id" in request.view_args:
        id = request.view_args['id']

    result = db['movies'].find_one(
        {"title": id})

    res = json.loads(json_util.dumps(result))

    return jsonify(data=res)

@netflix_api.route("/<string:id>", methods=["PATCH"])   # patch means to Update the objects in the collection based on the provided title
def update_movie(id):
    if "id" in request.view_args:
        id = request.view_args['id']

    data = request.get_json()

    req_body = {}

    if 'description' in data:
        req_body['description'] = data['description']

    if 'id' in data:
        req_body['id'] = data['id']

    if 'imdb_score' in data:
        req_body['imdb_score'] = data['imdb_score']

    if 'runtime' in data:
        req_body['runtime'] = data['runtime']

    if 'title' in data:
        req_body['title'] = data['title']

    result = db['movies'].find_one_and_update(
        {"title": id}, {"$set": req_body}, new=True)   # Updates the collection based on the matched title in the data

    res = json.loads(json_util.dumps(result))

    return jsonify(data=res)


@netflix_api.route("/<string:id>", methods=["DELETE"])    # Deletes collection based on the provided title
def delete_movie(id):
    if "id" in request.view_args:
        id = request.view_args['id']

    result = db['movies'].find_one_and_delete(
        {"title": id})

    res = json.loads(json_util.dumps(result))

    return jsonify(data=res)



    res = {
        'Null': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }
    
    count = 0
    
    for movie in db['movies'].find({}):
        count += 1
        # print("Count...", count)
        if 'imdb_score' not in movie:
            res['Null'] += 1
            continue
            
        if movie['imdb_score'] >= 1 and movie['imdb_score'] < 2:
            res['1'] += 1
        
        if movie['imdb_score'] >= 2 and movie['imdb_score'] < 3:
            res['2'] += 1
        
        if movie['imdb_score'] >= 3 and movie['imdb_score'] < 4:
            res['3'] += 1
        
        if movie['imdb_score'] >= 4 and movie['imdb_score'] < 5:
            res['4'] += 1
        
        if movie['imdb_score'] >= 5 and movie['imdb_score'] < 6:
            res['5'] += 1
        
        if movie['imdb_score'] >= 6 and movie['imdb_score'] < 7:
            res['6'] += 1
        
        if movie['imdb_score'] >= 7 and movie['imdb_score'] < 8:
            res['7'] += 1
        
        if movie['imdb_score'] >= 8 and movie['imdb_score'] < 9:
            res['8'] += 1
        
        if movie['imdb_score'] >= 9:
            res['9'] += 1
        
    # res = json.loads(json_util.dumps(res))

    return jsonify(data=res)
    
   # return render_template('imdb.html', res=res)

