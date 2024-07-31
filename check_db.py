from app import create_app, db
from sqlalchemy import inspect
import os

app = create_app()

with app.app_context():
    # Check if the database file exists
    db_file = os.path.join(app.instance_path, 'test.db')
    print(f"Database file exists: {os.path.exists(db_file)}")

    # Create tables
    print("Creating tables...")
    db.create_all()
    print("Tables created")

    # List tables in the database
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)
