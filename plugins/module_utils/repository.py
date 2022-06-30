from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreRepository(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/repositories"

    # Attributes
    attrs = SemaphoreProjectComponent.attrs | {
        "git_url": str,
        "git_branch": str,
        "ssh_key_id": int
    }
