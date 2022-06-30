from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreInventory(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/inventory"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        type=dict(type="str", required=True, choices=["static", "file"]),
        inventory=dict(type="str", required=True),
    )
