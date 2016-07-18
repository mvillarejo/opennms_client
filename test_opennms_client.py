# -*- coding: utf-8 -*-

"""
Tests for opennms_client
~~~~~~~~~~~~~~~~~~~~~~~~
All these test are quite tight to http://demo.opennms.org/opennms, a small change there can cause errors.

"""

import unittest

import opennms_client
from opennms_client.exceptions import OpenNMSClientConnectError, ServiceDoesNotExistInNodeError


class OpenNMSClientTestCase(unittest.TestCase):

    # _multiprocess_can_split_ = True

    def setUp(self):
        self.client = opennms_client.OpenNMSClient("https://demo.opennms.org/opennms", "demo", "demo")

    def tearDown(self):
        pass

    def testEntryPoints(self):
        opennms_client.OpenNMSClient

    def testInvalidHost(self):
        self.assertRaises(OpenNMSClientConnectError, opennms_client.OpenNMSClient, "http://demo.opennms.org", "non_user", "non_password")

    def testGetNodes(self):
        self.client.get_nodes()
        self.assertEqual(self.client.nodes[0]["label"], "accounts.internal.opennms.com")

    def testGetNode(self):
        self.assertEqual(self.client.get_node("demo.opennms.org")["label"], "demo.opennms.org")

    def testGetNodeIpInterface(self):
        self.assertIn("96.17.15.43", [ip_interface['ipAddress'] for ip_interface in self.client.get_node_ipinterfaces("www.nasdaq.com")])

    def testGetNodeIpInterfacePrincipal(self):
        self.assertIn("174.143.250.51", self.client.get_node_ipinterface_principal("sync.opennms.com")['ipAddress'])

    def testGetServices(self):
        self.client.get_services()
        self.assertEqual(self.client.services["ICMP"], 1)

    def testGetNodeServices(self):
        self.assertIn("HTTP", [service['serviceType']['name'] for service in self.client.get_node_services("sync.opennms.com")])

    def testGetNodeServicesList(self):
        self.assertIn("HTTP", self.client.get_node_services_list("sync.opennms.com"))


    def testDeleteNodeServiceDoesNotExistInNode(self):
        self.assertRaises(ServiceDoesNotExistInNodeError, self.client.delete_node_service, "sync.opennms.com", "NTP")



if __name__ == '__main__':
    unittest.main()
