from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .models import Link
from .forms import ShortenerForm

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    
    return redirect(link.original_url)


@short.route('/')
def index():
    form = ShortenerForm()
    
    return render_template('index.html', form=form)

@short.route('/add_link', methods=['POST'])
def add_link(short_url=''):
    form = ShortenerForm()
    
    if form.validate_on_submit():
        original_url = request.form['original_url']
        
        if 'short_url' in request.form:
            short_url = request.form['short_url']
        
        link = Link(original_url=original_url, short_url=short_url)
        db.session.add(link)
        db.session.commit()

        return render_template('link_added.html', 
            new_link=link.short_url, original_url=link.original_url, form=form)
    
    return redirect('/')

@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404