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
        self.client = opennms_client.OpenNMSClient("http://demo.opennms.org/opennms", "demo", "demo")

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
        self.assertEqual(self.client.get_node("www.amazon.com")["label"], "www.amazon.com")

    def testGetNodeIpInterface(self):
        self.assertIn("205.251.242.54", [ip_interface['ipAddress'] for ip_interface in self.client.get_node_ipinterfaces("www.amazon.com")])

    def testGetNodeIpInterfacePrincipal(self):
        self.assertIn("205.251.242.54", self.client.get_node_ipinterface_principal("www.amazon.com")['ipAddress'])

    def testGetServices(self):
        self.client.get_services()
        self.assertEqual(self.client.services["ICMP"], 1)

    def testGetNodeServices(self):
        self.assertIn("Amazon", [service['serviceType']['name'] for service in self.client.get_node_services("www.amazon.com")])

    def testGetNodeServicesList(self):
        self.assertIn("Amazon", self.client.get_node_services_list("www.amazon.com"))


    def testDeleteNodeServiceDoesNotExistInNode(self):
        self.assertRaises(ServiceDoesNotExistInNodeError, self.client.delete_node_service, "www.amazon.com", "ICMP")



if __name__ == '__main__':
    unittest.main()

