# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.accounts.v1.credential import CredentialList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Accounts

        :returns: V1 version of Accounts
        :rtype: V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._credentials = None

    @property
    def credentials(self):
        """
        :rtype: twilio.rest.accounts.v1.credential.CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1>'
