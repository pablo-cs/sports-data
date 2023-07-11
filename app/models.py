from flask_sqlalchemy import SQLAlchemy


#stuff for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///favplayer.db'
db = SQLAlchemy(app)


#database class for favorited players...only stores id of player
class Favplayer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False) #playerid
    #db.string illustrates max length
    #playerName = db.Column(db.String(120), unique=False, nullable=False) #how to address players with the same name? 

    #for checking right id 
    def __repr__(self):
        return f"User('{self.id}')"



#database class adds players who have been commented on along with their comments.... stores id, playername, username, and comment
class CommentPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    playername = db.Column(db2.string(30),unique=False, nullable = False)
    username = db.Column(db2.string(20), unique = True, nullable = False)
    comment = db.Column(db2.string(255), unique=False, nullable = False)

    #to check getting right info
    def __repr__(self):
        return f"User('{self.id}',{self.playername},{self.username},{self.comment})"

with app.app_context():
  db.create_all()



export FLASK_APP= app.py
# flask shell
# >>> from app import Player
# >>> player.query.all()