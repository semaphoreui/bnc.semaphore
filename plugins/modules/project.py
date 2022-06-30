#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's projects
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
module: project
short_description: Ansible module to interact with Semaphore's projects
description:
  - Creates, updates or removes project from Semaphore
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
extends_documentation_fragment:
  - bnc.semaphore.component
"""

EXAMPLES = r"""
---
# Create a project
- name: Create project
  bnc.semaphore.project:
    name: Test project
    state: present
    url: http://localhost:3000/api
    token: XXXX
"""

# pylint: disable=import-error,wrong-import-position
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.project import (
    SemaphoreProject,
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
        )
    )

    # Defer to project class
    semaphore = SemaphoreProject(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
