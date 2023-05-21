from . import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # relationships = db.relationship("MappedFiles", back_populates="users", uselist = False)

    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))

    username = db.Column(db.String(1000))

class OriginalFiles(UserMixin, db.Model):
    __tablename__ = 'original_files'

    file_id = db.Column(db.Integer, primary_key=True)
    # relationships = db.relationship("MappedFiles", back_populates="original_files", uselist = False)

    fileName = db.Column(db.String(200))

    md5 = db.Column(db.String(200))

class MappedFiles(UserMixin, db.Model):
    __tablename__ = 'mapped_files'

    mapped_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # users = db.relationship("Users", back_populates="mapped_files")

    fileName = db.Column(db.String(200))

    original_id = db.Column(db.Integer, db.ForeignKey('original_files.file_id'))
    # original_files = db.relationship("OriginalFiles", back_populates="mapped_files")