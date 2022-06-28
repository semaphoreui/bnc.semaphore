#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

"""
Ansible module to interact with Semaphore's projects
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": [
        "preview"
    ],
    "supported_by": "community"
}

DOCUMENTATION = r"""
---
module: project
short_description: Ansible module to interact with Semaphore's projects
description:
    - Creates, updates or removes project from Semaphore
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
version_added: 2.9.0
options:
  name:
    type: str
    required: true
    description: Project's name
  state:
    type: str
    description: Project state
    default: present
    choices:
      - present
      - absent
"""

EXAMPLES = r"""
---
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.semaphore.project import SemaphoreProject


def main():

    # Ansible module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=[
                    'present',
                    'absent'
                ]
            )
        )
    )

    # Defer to project class


if __name__ == "__main__":
    main()
