from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreRepository(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/repositories"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        git_url=dict(type="str", required=True),
        git_branch=dict(type="str", required=True),
        ssh_key_id=dict(type="int", required=True),
    )
