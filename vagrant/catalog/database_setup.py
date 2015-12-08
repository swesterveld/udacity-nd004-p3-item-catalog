from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    given_name = Column(String, nullable=True)
    family_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    picture = Column(String)
    gender = Column(String, nullable=True)


class Category(Base):
    '''Categories can have sub categories. The parent of a sub category is a
    category.'''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    parent_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    parent = relationship('Category')

    @property
    def serialize(self):
        '''Return object data in JSON format'''
        return {
            'id':           self.id,
            'parent_id':    self.parent_id,
            'name':         self.name,
            'description':  self.description,
            'items':        [i.serialize for i in self.items]
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref=backref('items', order_by=id))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('items', order_by=id))

    @property
    def serialize(self):
        '''Return object data in JSON format'''
        return {
            'id':           self.id,
            'name':         self.name,
            'description':  self.description,
            'category_id':  self.category_id,
            'user_id':      self.user_id
        }


engine = create_engine('postgresql+psycopg2://connoisseur:michaeljackson@localhost:5432/beercatalog')

Base.metadata.create_all(engine)
