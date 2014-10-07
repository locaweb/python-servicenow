from servicenow import Utils

ttl_cache=0

class Base(object):
    __table__ = None

    def __init__(self, Connection):
        self.Connection = Connection

    @Utils.cached(ttl=ttl_cache)
    def list_by_query(self, *args):
        return self.Connection._list_by_query(self.__table__, *args).json()

    @Utils.cached(ttl=ttl_cache)
    def list(self, *args):
        return self.Connection._list(self.__table__, *args).json()

    @Utils.cached(ttl=ttl_cache)
    def fetch_all(self, *args):
        return self.Connection._get(self.__table__, *args).json()

    @Utils.cached(ttl=ttl_cache)
    def fetch_one(self, *args):
        try:
            return self.fetch_all(*args)['records'][0]
        except IndexError:
            return {}

    def create(self, *args):
        return self.Connection._post(self.__table__, *args).json()

    def update(self, where, *args):
        return self.Connection._update(self.__table__, where, *args).json()

    def delete(self, *args):
        return self.Connection._delete(self.__table__, *args).json()

    def last_updated(self, minutes):
        metaon = {'sys_updated_on': 'Last %d minutes@javascript:gs.minutesAgoStart(%d)@javascript:gs.minutesAgoEnd(0)' % (minutes, minutes)}
        return self.Connection._get(self.__table__, meta={}, metaon=metaon).json()

class Call(Base):
    __table__ = 'u_new_call.do'

class Change(Base):
    __table__ = 'change_request.do'

class Group(Base):
    __table__ = 'sys_user_group.do'

class Incident(Base):
    __table__ = 'incident.do'

class Problem(Base):
    __table__ = 'problem.do'

class Request(Base):
    __table__ = 'u_request.do'

class Server(Base):
    __table__ = 'cmdb_ci_server.do'

class Ticket(Base):
    __table__ = 'u_service_desk.do'

class Task(Base):
        __table__ = 'task_ci_list.do'

