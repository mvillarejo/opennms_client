# -*- coding: utf-8 -*-

"""
opennms_client.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the set of client's exceptions.
"""


class OpenNMSClientError(RuntimeError):
    """There was an ambiguous exception that occurred while handling
    your request."""
    def __init__(self, code=None, reason=None, string=None):
        self.code = code
        self.reason = reason
        self.string = string


class UnknownError(OpenNMSClientError):
    """Unknown error, please report full log at
    https://github.com/mvillarejo/opennms_client/issues"""

class OpenNMSClientConnectError(OpenNMSClientError):
    """Can Not Connect to openNMS server"""

class NodeDoesNotExistError(OpenNMSClientError):
    """Node does not exist."""

class MoreThanOneNodeReturnedError(OpenNMSClientError):
    """More than one node was returned with query supplied."""

class MoreThanOneIpInterfaceReturnedError(OpenNMSClientError):
    """More than one ip interface was returned when only principal was requested."""

class ServiceDoesNotExistError(OpenNMSClientError):
    """Service does not exist."""

class ServiceDoesNotExistInNodeError(OpenNMSClientError):
    """Service does not exist in the node provided."""