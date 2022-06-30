from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreEnvironment(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/environment"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        password=dict(type="str", required=False, no_log=True),
        json=dict(type="json", required=True),
    )
