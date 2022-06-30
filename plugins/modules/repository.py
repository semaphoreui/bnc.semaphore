#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's repositories
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
module: repository
short_description: Ansible module to interact with Semaphore's repositories
description:
  - Creates, updates or removes repository from Semaphore's project
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
options:
  git_url:
    type: str
    required: true
    description: Repository URL
  git_branch:
    type: str
    required: true
    description: Repository branch
  ssh_key_id:
    type: int
    required: true
    description: SSH key to access repository
extends_documentation_fragment:
  - bnc.semaphore.component
  - bnc.semaphore.project_component
"""

EXAMPLES = r"""
---
# Creates a repository in project with ID 1
- name: Create repository
  bnc.semaphore.repository:
    name: Test repository
    state: present
    url: http://localhost:3000/api
    token: XXXX
    git_url: ssh://git@github.com/bnc-ch/aod_tasks.git
    git_branch: main
    ssh_key_id: 1
"""

# pylint: disable=import-error,wrong-import-position
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.repository import (
    SemaphoreRepository,
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
            git_url=dict(type="str", required=True),
            git_branch=dict(type="str", required=True),
            ssh_key_id=dict(type="int", required=True),
        )
    )

    # Defer to project class
    semaphore = SemaphoreRepository(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
