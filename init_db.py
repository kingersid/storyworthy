from app import create_app, db

# Create the app instance
app = create_app()

# Push the app context
with app.app_context():
    # Create all database tables
    db.create_all()
    print("Database created!")