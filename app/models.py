from flask_sqlalchemy import SQLAlchemy


#stuff for databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playerfavs.db'
db = SQLAlchemy(app)

#I want to save the key information for a favorited player from a GET request that returns a dictionary
#How will this databases always get the most current information for that player if its only storing a players data at that time of the request? 
#Will clicking on favorited player just start the GET request, if so how is the GET request tied to favorited player?
#possible database columns: player name, GET request or player name and then their stats
#is the database being used so the front end can easily grab the information to display?
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #db.string illustrates max length
    player = db.Column(db.String(120), unique=False, nullable=False) #how to address players with the same name? this can't be unique then?
    request = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.player}', '{self.request}')"

#creates table to use in routes
with app.app_context():
  db.create_all()



export FLASK_APP= app.py
# flask shell
# >>> from app import Player
# >>> player.query.all()