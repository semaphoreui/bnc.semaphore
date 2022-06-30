from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreKey(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = '/keys'

    # Attributes
    attrs = SemaphoreProjectComponent.attrs | {
        "type": str,
        "ssh": {
            "login": str,
            "passphare": str,
            "private_key": str
        },
        "login_password": {
            "login": str,
            "password": str
        },
        "override_secret": True
    }
