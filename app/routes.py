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
        headers = generate_headers()
        player_data = get_player_data(user_name, headers)
        if player_data:
            existing_player = Player.query.filter_by(
                                name=player_data['name']).first()
            player_exists = bool(existing_player)
            return render_template(
                    'results.html', player=player_data,
                    in_db=player_exists
                )
    return render_template('player.html', player=None, description=None)


def add():
    """
    Adds player to Player database
    """
    user_name = request.form.get('add_user')
    headers = generate_headers()
    player_data = get_player_data(user_name, headers)
    if player_data:
        existing_player = Player.query.filter_by(
                            name=player_data['name']).first()
        if not existing_player:
            player = Player(
                id=player_data['id'],
                name=player_data['first_name']+player_data['last_name']
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
    players = get_players(player_type)
    if player_type == 'fav':
        return render_template('favorites.html', players=players)
    else:
        return redirect(url_for('home'))
