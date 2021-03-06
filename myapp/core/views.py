from datetime import datetime

# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Cookout

core = Blueprint('core', __name__)

@core.route('/')
def index():
    print('index page')
    page = request.args.get('page', 1, type=int)
    cookouts = Cookout.query.filter(Cookout.date >= datetime.now()).order_by(Cookout.date.asc()).paginate(page=page, per_page=5)
    return render_template('index.html', cookouts=cookouts)
        
@core.route('/info')
def info():
    return render_template('info.html')