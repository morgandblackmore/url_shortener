import string
from random import choices
from .extensions import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.short_url:
            self.short_url = self.generate_short()
        else:
            self.short_url = self.generate_short(10)

    def generate_short(self,size=5):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=size))
        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short()
        
        return short_url