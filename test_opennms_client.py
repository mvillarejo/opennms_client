# -*- coding: utf-8 -*-

"""Tests for fut."""

import unittest

import opennms_client
from opennms_client.exceptions import OpenNMSClientConnectError


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

    def testGetServices(self):
        self.client.get_services()
        self.assertEqual(self.client.services["ICMP"], 1)

    # TODO: the API is not available online so can not test any further...


if __name__ == '__main__':
    unittest.main()

