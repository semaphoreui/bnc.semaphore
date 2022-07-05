from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent
)


__metaclass__ = type


class SemaphoreSchedule(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/schedules"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        template_id=dict(type="int", required=True),
        cron_format=dict(type="str", required=True),
    )
