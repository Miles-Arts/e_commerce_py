from flask import Blueprint 
from flask import jsonify
from flask import request
import uuid

#Entities
from models.entities.Movie import Movie

#models
from models.MovieModel import MovieModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        
        movies=MovieModel.get_movies()
        return jsonify(movies)
        
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/<id>')
def get_movie(id):
    try:
        
        movie=MovieModel.get_movie(id)
        if movie!=None:
            return jsonify(movie)
        else:
            return jsonify({}),404
        
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/add',methods=['POST'])
def add_movie():
    try:
        
        title=request.json['title']
        duration=int(request.json['duration'])
        released=request.json['released']
        
        id=uuid.uuid4()
        movie=Movie(str(id),title,duration,released)
        
        affected_rows=MovieModel.add_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"Error al insertar datos"}), 500
        
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/update/<id>',methods=['PUT'])
def apdate_movie(id):
    try:
        
        title=request.json['title']
        duration=int(request.json['duration'])
        released=request.json['released']
        
        movie=Movie(id,title,duration,released)
        
        affected_rows=MovieModel.update_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"Película no actualizada."}), 404
        
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500    

    
@main.route('/delete/<id>',methods=['DELETE'])
def delete_movie(id):
    try:
        
        movie=Movie(id)
        
        affected_rows=MovieModel.delete_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"Movie no eliminada"}), 404
        
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500







