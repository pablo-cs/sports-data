from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from config import Config
from access_api import get_player_data
from models import db, Favplayer, CommentPlayer
from routes import (
    home,
    search,
    add_fav,
    remove,
    view_fav,
    add_comment
)

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.route('/')(home)
app.route('/search', methods=['POST'])(search)
app.route('/add', methods=['POST'])(add_fav)
app.route('/remove', methods=['POST'])(remove)
app.route('/view_fav', methods=['GET', 'POST'])(view_fav)
app.route('/add_comment', methods=['POST'])(add_comment)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")