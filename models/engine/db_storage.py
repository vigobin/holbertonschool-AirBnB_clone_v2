#!/usr/bin/python3
"""Database storage"""


from sqlalchemy.orm import scoped_session
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """creates an engine"""

        user = ("HBNB_MYSQL_USER")
        password = ("HBNB_MYSQL_PWD")
        host = ("HBNB_MYSQL_HOST")
        database = ("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = ["User", "State", "City", "Amenity", "Place", "Review"]
        object_list = {}
        if cls == None:
            for i in classes:
                obj = self.__session.query(i)
                for j in obj:
                    object_list.update("{}.{}: {}".format(type(obj).__name__, j.id, j))
                                       
        else:
            obj = self.__session.query(cls).all()
            for i in obj:
                object_list.update("{}.{}: {}".format(type(cls).__name__, i.id, i))
            return object_list

    def new(self, obj=None):
        self.__session.add(obj)

    def save(self):
        self.__session.save()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    