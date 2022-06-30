from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreEnvironment(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/environment"

    # Attributes
    attrs = SemaphoreProjectComponent.attrs | {
        "password": str,
        "json": str,
    }
