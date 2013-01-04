class Base(object):
    __table__ = None

    def __init__(self, connection)
        self.connection = connection

    def get(self, params):
        return self.connection._get(self.__table__, params).json()

    def create(self, params):
        return self.connection._post(self.__table__, params).json()

class Server(Base):
    __table__ = 'cmdb_ci_server_list.do'

class Incident(Base):
    __table__ = 'incident.do'
