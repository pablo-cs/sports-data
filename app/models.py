from flask_sqlalchemy import SQLAlchemy


#stuff for database
db = SQLAlchemy()


#database class for favorited players...only stores id of player
class Favplayer(db.Model):
    __bind_key__ = 'favorite'
    player_id = db.Column(db.Integer, primary_key=True, nullable=False) #playerid
    #db.string illustrates max length
    player_name = db.Column(db.String(30), unique=False, nullable=False) #how to address players with the same name? 
    team_name = db.Column(db.String(30), unique=False, nullable=False)
    #for checking right id 
    def __repr__(self):
        return f"Player('{self.player_id}')"



#database class adds players who have been commented on along with their comments.... stores id, playername, username, and comment
class CommentPlayer(db.Model):
    __bind_key__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, unique=False, nullable = False)
    player_name = db.Column(db.String(30),unique=False, nullable = False)
    user_name = db.Column(db.String(20), unique = False, nullable = False)
    comment = db.Column(db.String(255), unique=False, nullable = False)

    #to check getting right info
    def __repr__(self):
        return f"Player('{self.player_id}',{self.playername},{self.username},{self.comment})"

# with app.app_context():
#   db.create_all()



# export FLASK_APP= app.py
# flask shell
# >>> from app import Player
# >>> player.query.all()