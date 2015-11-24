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
    >>> c.get_services()
    {u'Amazon': 35,
     u'BingSearch': 38,
     u'DNS': 12,
     u'Dell-OpenManage': 24,
     u'FTP': 10,
     u'GoogleSearch': 36,
    ...
    >>> c.set_service("www.amazon.com ", "ICMP")
    <Response [200]>



Requirements
============
.. code-block:: bash
    pip install -r requirements.txt


Releases
========
Download pre-built releases on the [releases](https://github.com/mvillarejo/opennms_client/releases) page

Contributors
============
[Manuel Villarejo](https://github.com/mvillarejo) - Core Development

License
=======
MIT License
