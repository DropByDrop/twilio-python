# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.preview.sync.service import ServiceList


class Sync(Version):

    def __init__(self, domain):
        """
        Initialize the Sync version of Preview

        :returns: Sync version of Preview
        :rtype: Sync
        """
        super(Sync, self).__init__(domain)
        self.version = 'Sync'
        self._services = None

    @property
    def services(self):
        """
        :rtype: twilio.rest.preview.sync.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync>'
