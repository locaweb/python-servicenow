from servicenow import Connection

def Incident(Connection.Auth):

    endpoint = 'incident.do'

    def get(number):
        return self._get(endpoint, {'number': number})
