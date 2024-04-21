from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Engine, text
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from werkzeug.security import check_password_hash


from datetime import datetime
import hashlib

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 
# class User(db.Model):
#     __tablename__ = 'User'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(200), nullable=False)
#     pwHash = db.Column(db.String(1000), nullable=False)
#     e_Mail = db.Column(db.String(200), nullable=False)
#     level = db.Column(db.Integer, nullable=False)
#     rating = db.relationship("Rating", backref="user")

class User2(db.Model):
    __tablename__ = 'User2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    pwHash = db.Column(db.String(1000), nullable=False)
    e_Mail = db.Column(db.String(200), nullable=False)
    level = db.Column(db.Integer, nullable=False)

# class Direction(db.Model):
#     __tablename__ = 'Direction'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(200), nullable=False)
#     movie = db.relationship("Movie", backref="direction")

# class Actor(db.Model):
#     __tablename__ = 'Actor'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(200), nullable=False)
#     movieActor = db.relationship("MovieActor", backref="actor")

# class Genre(db.Model):
#     __tablename__ = 'Genre'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(200))
#     movie = db.relationship("Movie", backref="genre")

# class Movie(db.Model):
#      __tablename__ = 'Movie'
#      id = db.Column(db.Integer, primary_key=True, autoincrement=True) #primary Key 
#      title = db.Column(db.String(200), nullable=False) # normal Atribute
#      description = db.Column(db.String(3000), nullable=True)
#      release = db.Column(db.DateTime(), nullable=False)
#      age_restriction = db.Column(db.Integer, nullable=False)
#      image_path = db.Column(db.String(500), nullable=True)
#      id_Genre = db.Column(db.Integer, db.ForeignKey("Genre.id"), nullable=False) # key from a other table
#      id_Direction = db.Column(db.Integer, db.ForeignKey("Direction.id"), nullable=False)
#      genre = db.relationship("Genre", backref="movie")
#      direction = db.relationship("Direction", backref="movie")
#      rating1 = db.relationship("Rating", backref="movie1")

# class Rating(db.Model):
#     __tablename__ = 'Rating'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     id_Movie = db.Column(db.Integer, db.ForeignKey("Movie.id"), nullable=False)
#     id_User = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
#     comment = db.Column(db.String(2000), nullable=True)
#     rating = db.Column(db.Integer, nullable=False)
#     date = db.Column(db.DateTime(), default=datetime.now, nullable=False)
#     movie1 = db.relationship("Movie", backref="rating1")
#     user = db.relationship("User", backref="rating")

# class MovieActor(db.Model):
#     __tablename__ = 'MovieActor'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     id_Movie = db.Column(db.Integer, db.ForeignKey("Movie.id"), nullable=False)
#     id_Actor = db.Column(db.Integer, db.ForeignKey("Actor.id"), nullable=False)
#     movie = db.relationship("Movie", backref="movieActor")
#     actor = db.relationship("Actor", backref="movieActor")

def hasher(password):
    password_bytes = password.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(password_bytes)
    password_hash = sha256.hexdigest()    
    return password_hash

def add_user(new_username, pw, new_e_mail, new_level):    
    new_user2 = User2(username = new_username, pwHash = hasher(pw), e_Mail = new_e_mail, level = new_level)
    db.session.add(new_user2)
    db.session.commit()

def login_user(email, pw):
    print("login_user")
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(User2).filter_by(e_Mail=email).first()
    print("Passwort vor dem Hashen:", pw)   
    pw_hashed = hasher(pw)
    print("Gehashtes Passwort:", pw_hashed)
    if user and (user.pwHash == pw_hashed):
        print("Benutzer gefunden:")
        return("match")
    else:
        return("no match")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "register":
            print("register")
            username = request.form.get("username")
            email = request.form.get("email")
            pw_hash = request.form.get("password")
            add_user(username, pw_hash, email, 1) 
            return redirect(url_for("index"))  
        elif action == "login":
            print("login")
            email = request.form.get("email")
            password = request.form.get("password")
            login_user(email, password)    
            return redirect(url_for("index")) 

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
            db.create_all()              
    app.run(debug=True)