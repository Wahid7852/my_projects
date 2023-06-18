from app import create_app
from os import path

if __name__ == "__main__":
    app = create_app()

    # Check if db.sqlite file exists or not. If not then create db.sqlite
    if not path.exists("app/db.sqlite"):
        print ("<------------>")
        print("Setting up Database ..")
        print ("<------------>")
        print()
        with app.app_context():
            from app import db
            db.create_all()
        print ("<------------>")
        print("Database Setup Completed ..")
        print ("<------------>")
        print()

    app.run(host ='127.0.0.1', port = 8080)