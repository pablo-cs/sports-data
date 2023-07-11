import git
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from access_api import search_player

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
    if user_name:
        player_data = get_player_data(player_name)
        if player_data:
            existing_player = Player.query.filter_by(
                                id=player_data['id']).first()
            player_exists = bool(existing_player)
            player_comments = get_comments(player_data['id'])
            return render_template(
                    'player.html', player=player_data,
                    comments=comments
                    in_db=player_exists
                )
    return render_template('player.html', player=None)


def add():
    """
    Adds player to Player database
    """
    user_name = request.form.get('add_user')
    player_data = get_player_data(user_name)
    if player_data:
        existing_player = Player.query.filter_by(
                            name=player_data['name']).first()
        if not existing_player:
            player = Player(
                id=player_data['id'],
                name=player_data['name']
            )
            add_to_db(player)
            
    return redirect(url_for('view_fav'))


def remove():
    """
    Removes a player from the Player database
    """
    name_to_remove = request.form.get('removed_user')
    player = Player.query.filter_by(name=name_to_remove).first()
    if player:
        remove_from_db(player)
        players = get_players('fav')
        return render_template('favorites.html', players=players)
    else:
        return redirect(url_for('home'))

def view_fav():
    """
    Returns webpage of a set of users
    """
    players = get_players()
    return render_template('favorites.html', players=players)

def add_comment():
    user_name = request.form.get('user_name')
    user_comment = request.form.get('user_comment')
    player_id = request.form.get('player_id')
    add_comment(player_id,user_name, user_comment)
    player_comments = get_comments(player_data['id'])
    return render_template(
            'player.html', player=player_data,
            comments=comments
            in_db=player_exists
        )

