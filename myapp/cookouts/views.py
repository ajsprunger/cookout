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
        cookout = Cookout(name=form.name.data, date=form.date.data, creator_id=current_user.id, description=form.description.data, location=form.location.data, food=form.food.data, drink=form.drink.data, attendees=form.attendees.data)
        db.session.add(cookout)
        db.session.commit()
        flash('Cookout Created')
        print('Cookout was created')
        return redirect(url_for('core.index'))
    return render_template('create_cookout.html', form=form) 

@cookouts.route('/<int:cookout_id>')
def cookout(cookout_id):
    cookout = Cookout.query.get_or_404(cookout_id) 
    print('COOKOUT', cookout.id)
    return render_template('cookout.html', name=cookout.name, date=cookout.date, description=cookout.description, creator=cookout.creator, location=cookout.location, food=cookout.food, drink=cookout.drink, attendees=cookout.attendees, post=cookout)

@cookouts.route('/<int:cookout_id>/update',methods=['GET','POST'])
@login_required
def update(cookout_id):
    cookout = Cookout.query.get_or_404(cookout_id)
    if cookout.creator != current_user:
        abort(403)
    form = CookoutForm()
    if form.validate_on_submit():
        cookout.name = form.name.data
        cookout.description = form.description.data
        cookout.date = form.date.data
        cookout.location = form.location.data
        cookout.food = form.food.data
        cookout.drink = form.drink.data
        cookout.attendees = form.attendees.data
        db.session.commit()
        flash('Cookout Updated')
        return redirect(url_for('cookouts.cookout',cookout_id=cookout.id))
    elif request.method == 'GET':
        form.name.data = cookout.name
        form.description.data = cookout.description
        form.date.data = cookout.date
        form.location.data = cookout.location
        form.food.data = cookout.food
        form.drink.data = cookout.drink
        form.attendees.data = cookout.attendees
    return render_template('create_cookout.html',title='Updating',form=form)

@cookouts.route('/<int:cookout_id>/delete',methods=['GET','POST'])
@login_required
def delete_cookout(cookout_id):
    cookout = Cookout.query.get_or_404(cookout_id)
    if cookout.creator != current_user:
        abort(403)
    db.session.delete(cookout)
    db.session.commit()
    flash('Cookout Deleted')
    return redirect(url_for('core.index'))