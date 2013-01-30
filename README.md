# Python ServiceNow
* http://wiki.servicenow.com/index.php?title=JSON_Web_Service

## Python Library to interact and manage the ServiceNow database

## Usage:
### Build the package

    $ dpkg-buildpackage -us -uc -rfakeroot
    $ dpkg -i python-servicenow-<version>.deb

### Using setup.py

    $ python setup.py build
    $ python setup.py install

### Example

    #!/usr/bin/python

    from servicenow import ServiceNow
    from servicenow import Connection

    conn = Connection.Auth(username='edsu', password='bele', instance='demo')
    inc = ServiceNow.Incident(conn)
    srv = ServiceNow.Server(conn)
    grp = ServiceNow.Group(conn)
    chg = ServiceNow.Change(conn)

    machine = srv.fetch_one({'name': 'machine0001'})
    print machine

    inc = inc.fetch_one({'number': 'INC123456'})
    print inc

    group = grp.fetch_one({'name': 'MY-Team'})
    print group

    changes = chg.fetch_all({'cmdb_ci': machine['sys_id'], 'review_status': 3})
    print changes

    ticket = tkt.fetch_one({'number': 'TICKET0185412'})
    print ticket

### Depends
* python-requests
* python-redis
