from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Optional, URL


class ShortenerForm(FlaskForm):
    original_url = URLField('Original Url', validators=[DataRequired(message='Valid URL required'),URL(require_tld=False, message='Valid URL required')])
    short_url = URLField('Short Url', validators=[Optional(),URL(require_tld=False, message='Valid URL required')])
    submit = SubmitField('Submit')