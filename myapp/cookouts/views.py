from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Cookout
from myapp.cookouts.forms import CookoutForm

cookouts = Blueprint('cookouts', __name__)

@cookouts.route('/create', methods=['GET', 'POST'])
@login_required
def create_cookout():
    form = CookoutForm()
    if form.validate_on_submit():
        cookout = Cookout(name=form.name.data, date=form.date.data, creator=current_user.id, description=form.description.data, location=form.location.data, food=form.food.data, drink=form.drink.data, attendees=form.attendees.data)
        db.session.add(cookout)
        db.session.commit()
        flash('Cookout Created')
        print('Cookout was created')
        return redirect(url_for('core.index'))
    return render_template('create_cookout.html', form=form)