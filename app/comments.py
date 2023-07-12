from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    comment = StringField('Comment',
                        validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Post Comment')