# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ActivityList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the ActivityList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        """
        super(ActivityList, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Activities'.format(**self._solution)

    def stream(self, friendly_name=values.unset, available=values.unset, limit=None,
               page_size=None):
        """
        Streams ActivityInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: The friendly_name
        :param unicode available: The available
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            friendly_name=friendly_name,
            available=available,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, available=values.unset, limit=None,
             page_size=None):
        """
        Lists ActivityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: The friendly_name
        :param unicode available: The available
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            friendly_name=friendly_name,
            available=available,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, available=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ActivityInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: The friendly_name
        :param unicode available: The available
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ActivityInstance
        :rtype: Page
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'Available': available,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ActivityPage(self._version, response, self._solution)

    def create(self, friendly_name, available=values.unset):
        """
        Create a new ActivityInstance

        :param unicode friendly_name: The friendly_name
        :param bool available: The available

        :returns: Newly created ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Available': available,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def get(self, sid):
        """
        Constructs a ActivityContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        return ActivityContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ActivityContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        return ActivityContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ActivityList>'


class ActivityPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ActivityPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        """
        super(ActivityPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ActivityInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ActivityPage>'


class ActivityContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the ActivityContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        super(ActivityContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Activities/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ActivityInstance

        :returns: Fetched ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset):
        """
        Update the ActivityInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the ActivityInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ActivityContext {}>'.format(context)


class ActivityInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the ActivityInstance

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        super(ActivityInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'available': payload['available'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ActivityContext for this ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        if self._context is None:
            self._context = ActivityContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def available(self):
        """
        :returns: The available
        :rtype: bool
        """
        return self._properties['available']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ActivityInstance

        :returns: Fetched ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the ActivityInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    def delete(self):
        """
        Deletes the ActivityInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ActivityInstance {}>'.format(context)
