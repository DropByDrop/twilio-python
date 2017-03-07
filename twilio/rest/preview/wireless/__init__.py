# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.preview.wireless.command import CommandList
from twilio.rest.preview.wireless.rate_plan import RatePlanList
from twilio.rest.preview.wireless.sim import SimList


class Wireless(Version):

    def __init__(self, domain):
        """
        Initialize the Wireless version of Preview

        :returns: Wireless version of Preview
        :rtype: Wireless
        """
        super(Wireless, self).__init__(domain)
        self.version = 'wireless'
        self._commands = None
        self._rate_plans = None
        self._sims = None

    @property
    def commands(self):
        """
        :rtype: twilio.rest.preview.wireless.command.CommandList
        """
        if self._commands is None:
            self._commands = CommandList(self)
        return self._commands

    @property
    def rate_plans(self):
        """
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanList
        """
        if self._rate_plans is None:
            self._rate_plans = RatePlanList(self)
        return self._rate_plans

    @property
    def sims(self):
        """
        :rtype: twilio.rest.preview.wireless.sim.SimList
        """
        if self._sims is None:
            self._sims = SimList(self)
        return self._sims

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless>'
