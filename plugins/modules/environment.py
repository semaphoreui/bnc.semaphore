#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's environments
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
module: environment
short_description: Ansible module to interact with Semaphore's environments
description:
  - Creates, updates or removes environment from Semaphore's project
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
options:
  password:
    type: str
    required: false
    description: Environment password
  json:
    type: json
    required: true
    description: Environment definition in JSON format
extends_documentation_fragment:
  - bnc.semaphore.component
  - bnc.semaphore.project_component
"""

EXAMPLES = r"""
---
# Creates an environment in project with ID 1
- name: Create environment
  bnc.semaphore.environment:
    name: Test environment
    state: present
    url: http://localhost:3000/api
    token: XXXX
    json: '{}'
"""

# pylint: disable=import-error,wrong-import-position
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.environment import (
    SemaphoreEnvironment,
)


def main():
    """
    Main function
    """

    # Ansible module
    module = AnsibleModule(
        argument_spec=SemaphoreEnvironment.argument_spec
    )

    # Defer to project class
    semaphore = SemaphoreEnvironment(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
