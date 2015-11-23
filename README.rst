==============
opennms-client
==============

.. image:: https://travis-ci.org/mvillarejo/opennms-client.png?branch=master
        :target: https://travis-ci.org/mvillarejo/opennms-client
.. image:: https://readthedocs.org/projects/opennms-client/badge/?version=latest
        :target: http://opennms-client.readthedocs.org/en/latest/?badge=latest


opennms-client is a simple package to manage openNMS.

Usage
=====

.. code-block:: python

    >>> import client
    >>> onms_client = client.Client("http://demo.opennms.org/opennms", "demo", "demo")
    >>> print onms_client
    http://demo.opennms.org/opennms (demo) <Response [200]>
    >>> onms_client.get_services()
    {u'Amazon': 35,
     u'BingSearch': 38,
     u'DNS': 12,
     u'Dell-OpenManage': 24,
     u'FTP': 10,
     u'GoogleSearch': 36,
    ...
    >>> onms_client.set_service("www.amazon.com ", "ICMP")
    <Response [200]>



Requirements
============
.. code-block:: bash
    pip install -r requirements.txt


Releases
========
Download pre-built releases on the [releases](https://github.com/mvillarejo/opennms-client/releases) page

Contributors
============
[Manuel Villarejo](https://github.com/mvillarejo) - Core Development

License
=======
MIT License
