from flask import Blueprint 
from flask import jsonify


main=Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    return jsonify({'message':"Aprendo Python"})









