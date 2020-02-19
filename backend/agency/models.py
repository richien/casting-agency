import os
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    func,
    distinct)
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta


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
    dob = Column(DateTime, nullable=False)
    gender = Column(String, nullable=False)
    movies = relationship('Movie', secondary=movie_actors, backref='actors')
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = datetime.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_age(self):
        today = datetime.now().date()
        days_in_year = 365.2425
        age = (today - self.dob.date()) // timedelta(days=days_in_year)
        return age

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.get_age(),
            'gender': self.gender,
            'created-at': self.created_at.isoformat(),
            'updated-at': self.updated_at.isoformat()
        }
    
    @classmethod
    def get_assigned_unassigned_totals(cls):
        assigned = db.session.query(
            func.count(
                distinct(Actor.id)).label('assigned')).filter(
                    Actor.id == movie_actors.c.actor_id).all()
        unassigned = db.session.query(
            func.count(
                distinct(Actor.id)).label('unassigned')).filter(
                    Actor.id != movie_actors.c.actor_id).all()
        return {
            'assigned': assigned[0].assigned,
            'unassigned': unassigned[0].unassigned
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = datetime.now()
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
            'release-date': self.release_date.isoformat(),
            'created-at': self.created_at.isoformat(),
            'updated-at': self.updated_at.isoformat()
        }
