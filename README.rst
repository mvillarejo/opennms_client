==============
opennms_client
==============

.. image:: https://travis-ci.org/mvillarejo/opennms_client.png?branch=master
        :target: https://travis-ci.org/mvillarejo/opennms_client
.. image:: https://readthedocs.org/projects/opennms_client/badge/?version=latest
        :target: http://opennms_client.readthedocs.org/en/latest/?badge=latest


opennms_client is a simple package to manage openNMS.

Usage
=====

.. code-block:: python

    >>> import opennms_client
    >>> c = opennms_client.OpenNMSClient("http://demo.opennms.org/opennms", "demo", "demo")
    >>> print c
    http://demo.opennms.org/opennms (demo) <Response [200]>
    >>> len(c.get_nodes())
    10
    >>> len(c.get_nodes(limit=0))
    56
    >>> c.get_services()
    {u'Amazon': 35,
     u'BingSearch': 38,
     u'DNS': 12,
     u'Dell-OpenManage': 24,
     u'FTP': 10,
     u'GoogleSearch': 36,
    ...
    >>> c.get_node("www.amazon.com")
    { ...
     u'createTime': 1355967495052,
     u'foreignId': u'1355756384535',
     u'foreignSource': u'Minimal Detectors',
     u'id': u'53',
     u'label': u'www.amazon.com',
     u'labelSource': u'U',
     u'lastCapsdPoll': 1447528445225,
     u'type': u'A'}
    >>> c.get_node_ipinterfaces("www.amazon.com")
    [{u'hostName': u'205.251.242.54',
      u'id': u'66463',
      u'ifIndex': None,
      u'ipAddress': u'205.251.242.54',
      u'isDown': False,
      u'isManaged': u'M',
      u'lastCapsdPoll': 1447528445225,
      u'monitoredServiceCount': 1,
      u'nodeId': 53,
      u'snmpPrimary': u'P'}]
    >>> In [21]: c.get_node_services("www.amazon.com")
    [{u'applications': [],
      u'down': False,
      u'lastFail': None,
      u'lastGood': None,
      u'notify': None,
      u'qualifier': None,
      u'serviceType': {u'id': 35, u'name': u'Amazon'},
      u'source': None,
      u'status': u'N',
      u'statusLong': u'Not Monitored'}]
    >>> c.get_node_services_list("www.amazon.com")
    [u'Amazon']
    >>> c.set_node_service("www.amazon.com ", "ICMP")
    <Response [200]>
    >>> c.delete_node("www.amazon.com")
    <Response [200]>



Requirements
============
.. code-block:: bash
    pip install -r requirements.txt


Errors
======
You might experience some errors tyring ot build ssl support, try this before installing:

Mac
.. code-block:: bash
    export LDFLAGS="-L$(brew --prefix openssl)/lib"
    export CFLAGS="-I$(brew --prefix openssl)/include"

Linux
.. code-block:: bash
    yum install gcc python-devel libffi-devel openssl-devel -y

Releases
========
Download pre-built releases on the [releases](https://github.com/mvillarejo/opennms_client/releases) page

Contributors
============
[Manuel Villarejo](https://github.com/mvillarejo) - Core Development

License
=======
MIT License
