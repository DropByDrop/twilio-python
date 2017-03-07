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
from twilio.rest.taskrouter.v1.workspace.task.reservation import ReservationList


class TaskList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the TaskList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskList
        """
        super(TaskList, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks'.format(**self._solution)

    def stream(self, priority=values.unset, assignment_status=values.unset,
               workflow_sid=values.unset, workflow_name=values.unset,
               task_queue_sid=values.unset, task_queue_name=values.unset,
               evaluate_task_attributes=values.unset, ordering=values.unset,
               has_addons=values.unset, limit=None, page_size=None):
        """
        Streams TaskInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode priority: The priority
        :param unicode assignment_status: The assignment_status
        :param unicode workflow_sid: The workflow_sid
        :param unicode workflow_name: The workflow_name
        :param unicode task_queue_sid: The task_queue_sid
        :param unicode task_queue_name: The task_queue_name
        :param unicode evaluate_task_attributes: The evaluate_task_attributes
        :param unicode ordering: The ordering
        :param bool has_addons: The has_addons
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
            priority=priority,
            assignment_status=assignment_status,
            workflow_sid=workflow_sid,
            workflow_name=workflow_name,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            evaluate_task_attributes=evaluate_task_attributes,
            ordering=ordering,
            has_addons=has_addons,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset,
             evaluate_task_attributes=values.unset, ordering=values.unset,
             has_addons=values.unset, limit=None, page_size=None):
        """
        Lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode priority: The priority
        :param unicode assignment_status: The assignment_status
        :param unicode workflow_sid: The workflow_sid
        :param unicode workflow_name: The workflow_name
        :param unicode task_queue_sid: The task_queue_sid
        :param unicode task_queue_name: The task_queue_name
        :param unicode evaluate_task_attributes: The evaluate_task_attributes
        :param unicode ordering: The ordering
        :param bool has_addons: The has_addons
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
            priority=priority,
            assignment_status=assignment_status,
            workflow_sid=workflow_sid,
            workflow_name=workflow_name,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            evaluate_task_attributes=evaluate_task_attributes,
            ordering=ordering,
            has_addons=has_addons,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset,
             evaluate_task_attributes=values.unset, ordering=values.unset,
             has_addons=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param unicode priority: The priority
        :param unicode assignment_status: The assignment_status
        :param unicode workflow_sid: The workflow_sid
        :param unicode workflow_name: The workflow_name
        :param unicode task_queue_sid: The task_queue_sid
        :param unicode task_queue_name: The task_queue_name
        :param unicode evaluate_task_attributes: The evaluate_task_attributes
        :param unicode ordering: The ordering
        :param bool has_addons: The has_addons
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: Page
        """
        params = values.of({
            'Priority': priority,
            'AssignmentStatus': assignment_status,
            'WorkflowSid': workflow_sid,
            'WorkflowName': workflow_name,
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'EvaluateTaskAttributes': evaluate_task_attributes,
            'Ordering': ordering,
            'HasAddons': has_addons,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return TaskPage(self._version, response, self._solution)

    def create(self, timeout=values.unset, priority=values.unset,
               task_channel=values.unset, workflow_sid=values.unset,
               attributes=values.unset):
        """
        Create a new TaskInstance

        :param unicode timeout: The timeout
        :param unicode priority: The priority
        :param unicode task_channel: The task_channel
        :param unicode workflow_sid: The workflow_sid
        :param unicode attributes: The attributes

        :returns: Newly created TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        data = values.of({
            'Timeout': timeout,
            'Priority': priority,
            'TaskChannel': task_channel,
            'WorkflowSid': workflow_sid,
            'Attributes': attributes,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def get(self, sid):
        """
        Constructs a TaskContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        return TaskContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a TaskContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        return TaskContext(
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
        return '<Twilio.Taskrouter.V1.TaskList>'


class TaskPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TaskPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        """
        super(TaskPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return TaskInstance(
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
        return '<Twilio.Taskrouter.V1.TaskPage>'


class TaskContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the TaskContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        super(TaskContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{sid}'.format(**self._solution)

        # Dependents
        self._reservations = None

    def fetch(self):
        """
        Fetch a TaskInstance

        :returns: Fetched TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset,
               task_channel=values.unset):
        """
        Update the TaskInstance

        :param unicode attributes: The attributes
        :param task.status assignment_status: The assignment_status
        :param unicode reason: The reason
        :param unicode priority: The priority
        :param unicode task_channel: The task_channel

        :returns: Updated TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        data = values.of({
            'Attributes': attributes,
            'AssignmentStatus': assignment_status,
            'Reason': reason,
            'Priority': priority,
            'TaskChannel': task_channel,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the TaskInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        """
        if self._reservations is None:
            self._reservations = ReservationList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_sid=self._solution['sid'],
            )
        return self._reservations

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskContext {}>'.format(context)


class TaskInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the TaskInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        super(TaskInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'age': deserialize.integer(payload['age']),
            'assignment_status': payload['assignment_status'],
            'attributes': payload['attributes'],
            'addons': payload['addons'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'priority': deserialize.integer(payload['priority']),
            'reason': payload['reason'],
            'sid': payload['sid'],
            'task_queue_sid': payload['task_queue_sid'],
            'task_queue_friendly_name': payload['task_queue_friendly_name'],
            'task_channel_sid': payload['task_channel_sid'],
            'task_channel_unique_name': payload['task_channel_unique_name'],
            'timeout': deserialize.integer(payload['timeout']),
            'workflow_sid': payload['workflow_sid'],
            'workflow_friendly_name': payload['workflow_friendly_name'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
            'links': payload['links'],
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

        :returns: TaskContext for this TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        if self._context is None:
            self._context = TaskContext(
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
    def age(self):
        """
        :returns: The age
        :rtype: unicode
        """
        return self._properties['age']

    @property
    def assignment_status(self):
        """
        :returns: The assignment_status
        :rtype: task.status
        """
        return self._properties['assignment_status']

    @property
    def attributes(self):
        """
        :returns: The attributes
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def addons(self):
        """
        :returns: The addons
        :rtype: unicode
        """
        return self._properties['addons']

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
    def priority(self):
        """
        :returns: The priority
        :rtype: unicode
        """
        return self._properties['priority']

    @property
    def reason(self):
        """
        :returns: The reason
        :rtype: unicode
        """
        return self._properties['reason']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_queue_sid(self):
        """
        :returns: The task_queue_sid
        :rtype: unicode
        """
        return self._properties['task_queue_sid']

    @property
    def task_queue_friendly_name(self):
        """
        :returns: The task_queue_friendly_name
        :rtype: unicode
        """
        return self._properties['task_queue_friendly_name']

    @property
    def task_channel_sid(self):
        """
        :returns: The task_channel_sid
        :rtype: unicode
        """
        return self._properties['task_channel_sid']

    @property
    def task_channel_unique_name(self):
        """
        :returns: The task_channel_unique_name
        :rtype: unicode
        """
        return self._properties['task_channel_unique_name']

    @property
    def timeout(self):
        """
        :returns: The timeout
        :rtype: unicode
        """
        return self._properties['timeout']

    @property
    def workflow_sid(self):
        """
        :returns: The workflow_sid
        :rtype: unicode
        """
        return self._properties['workflow_sid']

    @property
    def workflow_friendly_name(self):
        """
        :returns: The workflow_friendly_name
        :rtype: unicode
        """
        return self._properties['workflow_friendly_name']

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

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a TaskInstance

        :returns: Fetched TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return self._proxy.fetch()

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset,
               task_channel=values.unset):
        """
        Update the TaskInstance

        :param unicode attributes: The attributes
        :param task.status assignment_status: The assignment_status
        :param unicode reason: The reason
        :param unicode priority: The priority
        :param unicode task_channel: The task_channel

        :returns: Updated TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return self._proxy.update(
            attributes=attributes,
            assignment_status=assignment_status,
            reason=reason,
            priority=priority,
            task_channel=task_channel,
        )

    def delete(self):
        """
        Deletes the TaskInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        """
        return self._proxy.reservations

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskInstance {}>'.format(context)
