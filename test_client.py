# -*- coding: utf-8 -*-

"""Tests for fut."""

import unittest

import client
from client.exceptions import OpenNMSClientConnectError


class OpenNMSClientTestCase(unittest.TestCase):

    # _multiprocess_can_split_ = True

    def setUp(self):
        self.client = client.Client("http://demo.opennms.org/opennms", "demo", "demo")

    def tearDown(self):
        pass

    def testEntryPoints(self):
        client.Client

    def testInvalidHost(self):
        self.assertRaises(OpenNMSClientConnectError, client.Client, "http://demo.opennms.org", "non_user", "non_password")

    def testGetServices(self):
        self.client.get_services()
        self.assertEqual(self.client.services["ICMP"], 1)

    # TODO: the API is not available online so can not test any further...


if __name__ == '__main__':
    unittest.main()

