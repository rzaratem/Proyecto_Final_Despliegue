from flask import Flask, render_template, url_for, request, session, flash, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
#from werkzeug.security import generate_password_hash, check_password_hash
from db import db, init_db
from dotenv import load_dotenv
from flask import jsonify, Blueprint
 
from models.heladeria import User,Producto
from controllers.heladeria_controller import heladeria_blueprint
from controllers.producto_controller import producto_blueprint
#from controllers.guarderia_controller import guarderias_routes
 
 
import os
 
load_dotenv() 
 
app = Flask(__name__)
 
app=Flask(__name__,template_folder='views')
 
app.register_blueprint(heladeria_blueprint)
app.register_blueprint(producto_blueprint)
 
 
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
global COOKIE_TIME_OUT
#COOKIE_TIME_OUT = 60*60*24*7 #7 days
COOKIE_TIME_OUT =  60*1 #60*5 #5 minutes
 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devdb.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "caircocoders-ednalan-2020"
 
 
 
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_STRING_CONNECTION')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print(app.config["SQLALCHEMY_DATABASE_URI"])

#db = SQLAlchemy(app)
db.init_app(app)
init_db(app)


#guarderias_routes(app)





  
if __name__ == '__main__':
    app.run(debug=True)
  

 
#from app import views, models