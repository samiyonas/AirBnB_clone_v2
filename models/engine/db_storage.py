#!/usr/bin/python3
""" DBStorage for AirBnB clone version 2 """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Database storage class """
    __engine = None
    __session = None

    classes = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}"
                .format(user, passwd, host, db), pool_pre_ping=True
                )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current db session all cls objects
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        '''
        dct = {}
        if cls is None:
            for c in DBStorage.classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        if "_sa_instance_state" in dct:
            del dct["_sa_instance_state"]
        return dct

    def new(self, obj):
        """ add the object to the current session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables and create the current session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ close the session """
        self.__session.close()
