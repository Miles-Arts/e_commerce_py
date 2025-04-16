from flask import Flask
from config import config
from flask_cors import CORS

#Routes
from routes import Movie

app=Flask(__name__)

#CORS(app, resources={"*":{"origins":"http://localhost:3000"}})

def page_not_found(error):
     return "<h1>No Funciona la página</h1><br><h4>Comuniquese con soporte</h4>", 404

if __name__=="__main__":
     app.config.from_object(config['development'])
     
     #Blueprints
     app.register_blueprint(Movie.main, url_prefix='/api/movies')
     
     
     #error hanslers
     app.register_error_handler(404, page_not_found)
     app.run()
     
     
     
     
     
     