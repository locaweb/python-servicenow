from servicenow import Utils

class Base(object):
    __table__ = None

    def __init__(self, Connection):
        self.Connection = Connection

    @Utils.cached(ttl=1)
    def list_by_query(self, *args):
        return self.Connection._list_by_query(self.__table__, *args).json()

    @Utils.cached(ttl=1)
    def list(self, *args):
        return self.Connection._list(self.__table__, *args).json()

    @Utils.cached(ttl=1)
    def fetch_all(self, *args):
        return self.Connection._get(self.__table__, *args).json()

    @Utils.cached()
    def fetch_one(self, *args):
        try:
            return self.Connection._get(self.__table__, *args).json()['records'][0]
        except IndexError:
            return {}

    def create(self, *args):
        return self.Connection._post(self.__table__, *args).json()

    def update(self, where, *args):
        return self.Connection._update(self.__table__, where, *args).json()

    def delete(self, *args):
        return self.Connection._delete(self.__table__, *args).json()

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

class Problem(Base):
    __table__ = 'problem.do'
