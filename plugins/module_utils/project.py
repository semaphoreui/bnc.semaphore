from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreComponent,
)


__metaclass__ = type


class SemaphoreProject(SemaphoreComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = '/project'

    # Ansible module argument_spec
    argument_spec = SemaphoreComponent.argument_spec
