#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Catalog(Base):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in  serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    catalog_id = Column(Integer, ForeignKey(Catalog.id))
    catalog = relationship(Catalog)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course

        }


engine = create_engine("sqlite:///catalog.db")
Base.metadata.create_all(engine)
