from flask import Blueprint, request, jsonify, redirect, url_for
from app import db
from app.models.entry import Entry
from datetime import datetime
from flask import render_template

entry_routes = Blueprint('entry_routes', __name__)





@entry_routes.route('/entries', methods=['GET'])
@entry_routes.route('/entries', methods=['GET'])
def get_entries():
    entries = Entry.query.order_by(Entry.date.desc()).all()  # Sort by date (newest first)
    return render_template('entries.html', entries=entries)



@entry_routes.route('/entries', methods=['POST'])
def add_entry():
    data = request.form  # Use request.form for form data
    new_entry = Entry(
        title=data['title'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),  # Parse date from form
        location=data['location'],
        story=data['story'],
        tags=data['tags']
    )
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('entry_routes.get_entries'))  # Redirect to the entries page

@entry_routes.route('/add', methods=['GET'])
def add_entry_form():
    return render_template('add_entry.html')


@entry_routes.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@entry_routes.route('/entries/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)  # Find the entry or return 404
    db.session.delete(entry)  # Delete the entry
    db.session.commit()  # Save changes to the database
    return redirect(url_for('entry_routes.get_entries'))  # Redirect to the entries page