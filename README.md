Python ServiceNow
=================

This is a Python Library to interact and manage the ServiceNow database via
[JSON web service](http://wiki.servicenow.com/index.php?title=JSONv2_Web_Service).

Installation:
------

### Using dpkg

    $ dpkg-buildpackage -us -uc -rfakeroot
    $ dpkg -i python-servicenow-<version>.deb

### Using setup.py

    $ python setup.py build
    $ python setup.py install

### Using pip

    $ pip install servicenow 

Usage:
------

### Example

    #!/usr/bin/python

    from servicenow import ServiceNow
    from servicenow import Connection

    conn = Connection.Auth(username='edsu', password='bele', instance='servicenowsubdomain')
    inc = ServiceNow.Incident(conn)
    srv = ServiceNow.Server(conn)
    grp = ServiceNow.Group(conn)
    chg = ServiceNow.Change(conn)
    tkt = ServiceNow.Ticket(conn)

    # Custom table
    custom = ServiceNow.Base(conn)
    custom.__table__ = "custom_table.do"

    machine = srv.fetch_one({'name': 'machine0001'})
    print machine

    inc = inc.fetch_one({'number': 'INC123456'})
    print inc

    group = grp.fetch_one({'name': 'MY-Team'})
    print group

    changes = chg.fetch_all({'cmdb_ci': machine['sys_id'], 'review_status': 3})
    print changes

    # list only sys_ids
    changes = chg.list({'cmdb_ci': machine['sys_id'], 'review_status': 3})
    print changes

    ticket = tkt.fetch_one({'number': 'TICKET0185412'})
    print ticket

    # Creating a new ticket based on another one
    del ticket["number"]
    new_ticket = tkt.create(ticket)
    print ticket

Dependencies:
------

- python-requests
- python-redis

Contributors:
------

- Juliano Martinez [ncode](https://github.com/ncode)
- James Stewart [amorphic](https://github.com/amorphic)
- Willian Molinari [Pothix](https://github.com/PotHix)
- Francisco Wagner Cunha Freire [wgrcunha](https://github.com/wgrcunha)

