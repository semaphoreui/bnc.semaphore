#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's keys
"""

from __future__ import absolute_import, division, print_function


# pylint: disable=invalid-name
__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: key
short_description: Ansible module to interact with Semaphore's keys
description:
  - Creates, updates or removes key from Semaphore's project
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
options:
  type:
    type: str
    description: Type of key
    required: true
    choices:
      - none
      - ssh
      - login_password
  ssh:
    type: dict
    description: Key properties when key's type is ssh
    required: false
    suboptions:
      private_key:
        type: str
        description: Private key content in OpenSSH format
        required: true
extends_documentation_fragment:
  - bnc.semaphore.component
  - bnc.semaphore.project_component
"""

EXAMPLES = r"""
---
# Creates an SSH key in project with ID 1
- name: Create SSH key
  bnc.semaphore.key:
    name: Test key
    state: present
    url: http://localhost:3000/api
    token: XXXX
    type: ssh
    ssh:
      private_key: XXXX
"""

# pylint: disable=import-error,wrong-import-position
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.key import (
    SemaphoreKey,
)


def main():
    """
    Main function
    """

    # Ansible module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
            url=dict(type="str", required=True),
            token=dict(type="str", required=True, no_log=True),
            project_id=dict(type="int", required=True),
            type=dict(
                type="str", required=True, choices=["none", "ssh", "login_password"]
            ),
            ssh=dict(
                type="dict",
                required=False,
                options=dict(private_key=dict(type="str", required=True, no_log=True)),
            ),
        )
    )

    # Defer to project class
    semaphore = SemaphoreKey(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
