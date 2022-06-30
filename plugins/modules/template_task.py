#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's templates
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
module: template_task
short_description: Ansible module to interact with Semaphore's templates
description:
  - Creates, updates or removes template from Semaphore's project
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
extends_documentation_fragment:
  - bnc.semaphore.component
  - bnc.semaphore.project_component
  - bnc.semaphore.template
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
from ansible_collections.bnc.semaphore.plugins.module_utils.template import (
    SemaphoreTemplateTask,
)


def main():
    """
    Main function
    """

    # Ansible module
    module = AnsibleModule(argument_spec=SemaphoreTemplateTask.argument_spec)

    # Defer to project class
    semaphore = SemaphoreTemplateTask(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
