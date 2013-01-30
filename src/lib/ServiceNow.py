from servicenow import Utils

class Base(object):
    __table__ = None

    def __init__(self, Connection):
        self.Connection = Connection

    @Utils.cached()
    def fetch_all(self, params):
        return self.Connection._get(self.__table__, params).json()

    @Utils.cached()
    def fetch_one(self, params):
        return self.Connection._get(self.__table__, params).json()['records'][0]

    def create(self, params):
        return self.Connection._post(self.__table__, params).json()

    def update(self, where, params):
        return self.Connection._update(self.__table__, where, params).json()

    def delete(self, params):
        return self.Connection._delete(self.__table__, params).json()

class Server(Base):
    __table__ = 'cmdb_ci_server.do'

class Incident(Base):
    __table__ = 'incident.do'

class Group(Base):
    __table__ = 'sys_user_group.do'

class Change(Base):
    __table__ = 'change_request.do'

class Ticket(Base):
    __table__ = 'u_service_desk.do'
