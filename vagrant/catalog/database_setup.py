from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    picture = Column(String)


class Category(Base):
    '''Categories can have sub categories. The parent of a sub category is a
    category.'''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    parent = relationship('Category')

    @property
    def serialize(self):
        '''Return object data in JSON format'''
        return {
            'id'    : id,
            'name'  : name
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        '''Return object data in JSON format'''
        return {
            'id'    : id,
            'name'  : name
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
