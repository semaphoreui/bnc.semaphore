#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2022 BNC Business Network Communications AG
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to interact with Semaphore's schedules
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
module: schedule
short_description: Ansible module to interact with Semaphore's schedules
description:
  - Creates, updates or removes schedule from Semaphore's project
author:
  - Alexandre Georges <alexandre.georges@bnc.ch> (@mageo)
options:
  template_id:
    type: int
    required: true
    description: Template ID
  cron_format:
    type: str
    required: true
    description: Cron string
extends_documentation_fragment:
  - bnc.semaphore.component
  - bnc.semaphore.project_component
"""

EXAMPLES = r"""
---
# Creates a schedule in project with ID 1 for task template with ID 1
- name: Create schedule
  bnc.semaphore.schedule:
    name: Test schedule
    state: present
    url: http://localhost:3000/api
    token: XXXX
    project_id: 1
    template_id: 1
    cron_format: "*/5 * * * *"
"""

# pylint: disable=import-error,wrong-import-position
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bnc.semaphore.plugins.module_utils.schedule import (
    SemaphoreSchedule
)


def main():
    """
    Main function
    """

    # Ansible module
    module = AnsibleModule(argument_spec=SemaphoreSchedule.argument_spec)

    # Defer to project class
    semaphore = SemaphoreSchedule(module)
    semaphore.handle()


if __name__ == "__main__":
    main()
