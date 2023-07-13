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
                                player_id=player_data['id']).first()
            player_exists = bool(existing_player)
            form = CommentForm()
            player_comments = CommentPlayer.query.filter_by(player_id=player_data['id']).all()
            return render_template(
                    'athlete.html', player=player_data,
                    comments=player_comments,
                    form=form,
                    in_db=player_exists
                )
    return render_template('athlete.html', player=None)


def add_fav():
    """
    Adds player to Favplayer database
    """
    player_name = request.form.get('added_player')
    player_data = get_player_data(player_name) 
    if player_data:
        existing_player = Favplayer.query.filter_by(
                            player_name=player_data['name']).first()
        if not existing_player:
            player = Favplayer(
                player_id=player_data['id'], 
                player_name=player_data['name'],
                team_name=player_data['team']['full_name']
            )
            db.session.add(player) #adds data to database
            db.session.commit()
            
    return redirect(url_for('view_fav'))


def remove():
    """
    Removes a player from the Favplayer database
    """
    id_to_remove = request.form.get('removed_player')
    player = Favplayer.query.filter_by(player_id=id_to_remove).first()
    if player:
        db.session.delete(player)
        db.session.commit()
    return redirect(url_for('view_fav'))


def view_fav():
    """
    Returns webpage of a set of users
    """
    players = Favplayer.query.all()
    #something like Favplayer.query.all() but then we only want to display names  and this query would get all the ids
    return render_template('favorites.html', players=players)

def add_comment():
    user_name = request.form.get('user_name')
    user_comment = request.form.get('user_comment')
    player_id = request.form.get('player_id')
    player_name = request.form.get('player_name')
    player_data = get_player_data(player_name)
    comment = CommentPlayer(player_id=player_id, player_name=player_name, user_name=user_name, comment=user_comment)
    db.session.add(comment)
    db.session.commit()
    form = CommentForm()
    player_comments = CommentPlayer.query.filter_by(player_id=player_id).all()
    return render_template(
        'athlete.html', player=player_data,
        comments=player_comments,
        form=form
    )



