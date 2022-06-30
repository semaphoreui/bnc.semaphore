from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreKey(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/keys"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        type=dict(type="str", required=True, choices=["none", "ssh", "login_password"]),
        ssh=dict(
            type="dict",
            required=False,
            options=dict(
                login=dict(type="str", required=False),
                passphrase=dict(type="str", required=False, no_log=True),
                private_key=dict(type="str", required=True, no_log=True),
            ),
        ),
        login_password=dict(
            type="dict",
            required=False,
            options=dict(
                login=dict(type="str", required=True),
                password=dict(type="str", required=True, no_log=True),
            ),
            no_log=False,
        ),
        override_secret=dict(type="bool", default=True),
    )
