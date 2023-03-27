#!/usr/bin/python3
"""Database storage"""


from sqlalchemy.orm import scoped_session
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """creates an engine"""

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

        classes = {"User": User, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Place": Place, "Review": Review}
        object_dict = {}
        if cls is None:
            for clas in classes.values():
                obj_list = self.__session.query(clas)
                for obj in obj_list:
                    object_dict.update("{}.{}: {}".format(
                        type(obj).__name__, obj.id, obj))

        else:
            obj = self.__session.query(cls).all()
            for i in obj:
                object_dict.update("{}.{}: {}".format(
                    type(cls).__name__, i.id, i))
        return object_dict

    def new(self, obj=None):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

    def close(self):
        """close session"""
        self.__session.close()
