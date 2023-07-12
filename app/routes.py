import git
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from access_api import get_player_data
from models import db, Favplayer, CommentPlayer
from comments import CommentForm

def home():
    """
    Returns the homepage for the application
    """
    return render_template('index.html')


# def webhook():
#     """
#     Webhook to automate the pushing of changes to the application repo
#     """
#     if request.method == 'POST':
#         repo = git.Repo('/home/')
#         origin = repo.remotes.origin
#         origin.pull()
#         return 'Updated PythonAnywhere successfully', 200
#     else:
#         return 'Wrong event type', 400


def search():
    """
    Returns the webpage of a given player, if it exists
    """
    player_name = request.form.get('search')
    if player_name:
        player_data = get_player_data(player_name)
        if player_data:
            existing_player = Favplayer.query.filter_by(
                                id=player_data['id']).first()
            player_exists = bool(existing_player)
            player_comments = get_comments(player_data['id'])
            return render_template(
                    'athlete.html', player=player_data,
                    comments=player_comments,
                    in_db=player_exists
                )
    return render_template('athlete.html', player=None)


def add_fav():
    """
    Adds player to Favplayer database
    """
    player_id = request.form.get('player_id')
    player_data = get_player_data(user_name) 
    if player_data:
        existing_player = Favplayer.query.filter_by(
                            name=player_data['name']).first()
        if not existing_player:
            player = Favplayer(
                id=player_data['id'], 
                name=player_data['name']
            )
            db.session.add(player) #adds data to database
            db.session.commit()
            
    return redirect(url_for('view_fav'))


def remove():
    """
    Removes a player from the Favplayer database
    """
    name_to_remove = request.form.get('removed_user')
    player = Favplayer.query.filter_by(name=name_to_remove).first()
    if player:
        db.session.delete(player)
        db.session.commit()
        players = get_players()
        return render_template('favorites.html', players=players)
    else:
        return redirect(url_for('home'))

def view_fav():
    """
    Returns webpage of a set of users
    """
    players = get_players()
    #something like Favplayer.query.all() but then we only want to display names  and this query would get all the ids
    return render_template('favorites.html', players=players)

def add_comment():
    user_name = request.form.get('user_name')
    user_comment = request.form.get('user_comment')
    player_id = request.form.get('player_id')
    add_comment(player_id,player_name, user_name, user_comment)
    comment = CommentPlayer(id=player_id, playername=xxxx,username=user_name,comment=user_comment) #need something for playername 
    db.session.add(comment)
    db.session.commit()
    player_comments = get_comments(player_data['id']) #would this be a query with the id ?
    return render_template(
            'athlete.html', player=player_data,
            comments=player_comments
        )

def get_comments(player_id):
    comments = CommentPlayer.query.filter_by(id=player_id).all()
    return comments

def get_players():
    favs = Favplayer.query.all()
    return favs


