.. :changelog:

Changelog
---------


0.1 (2015-11-20)
++++++++++++++++
* client: version 0.1

0.1.1 (2015-11-20)
++++++++++++++++++
* client: added set_service(hostname, service_name)

0.2 (2015-11-24)
++++++++++++++++
* Package renamed from opennms-client.client to opennms_client.opennms_client
* Fixed installation of dependencies using pip
* readthedocs.org documentation integrated now: http://opennms-client.readthedocs.org/en/latest/


0.2.1 (2015-11-24)
++++++++++++++++++
* delete_node(hostname)
* get_node_services,_list()
* delete_node_service(hostname, service_name)


0.2.2 (2016-03-9)
+++++++++++++++++
* set_node_service now has a index argument to set the service under interface you want to


0.2.3 (2016-03-9)
+++++++++++++++++
* added instructions to avoid SSL errors in Mac and Linux

0.3 (2016-07-18)
+++++++++++++++++
* added alarms to the class
