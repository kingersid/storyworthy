from datetime import datetime
from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100))
    story = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200))  # Comma-separated tags

    def __repr__(self):
        return f"<Entry {self.id}>"