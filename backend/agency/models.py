import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


database_uri = os.getenv('DATABASE_URI')

db = SQLAlchemy()


def setup_db(app, database_path=database_uri):
    """Binds a flask application and a SQLAlchemy service"""
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


movie_actors = db.Table(
        'movieactors',
        Column('actor_id', Integer, ForeignKey(
            'actors.id', ondelete='CASCADE'), primary_key=True),
        Column('movie_id', Integer, ForeignKey(
            'movies.id', ondelete='CASCADE'), primary_key=True)
    )


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    movies = relationship('Movie', secondary=movie_actors, backref='actors')

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add_actor(self, actor):
        self.actors.append(actor)
        db.session.commit()

    def delete_actor(self, actor):
        self.actors.remove(actor)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release-date': self.release_date.isoformat()
        }
