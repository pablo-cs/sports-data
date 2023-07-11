from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
#import models and routes

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
db.init_app(app)

with app.app_context():
    db.create_all()

#app.routes go here

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")