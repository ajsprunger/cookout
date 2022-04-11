# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Cookout

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    cookouts = Cookout.query.order_by(Cookout.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', cookouts=cookouts)
        
@core.route('/info')
def info():
    return render_template('info.html')