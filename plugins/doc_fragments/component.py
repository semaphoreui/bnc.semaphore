from __future__ import absolute_import, division, print_function

# pylint: disable=invalid-name
__metaclass__ = type


class ModuleDocFragment:
    """
    Base options for every Semaphore component
    """

    DOCUMENTATION = r"""
options:
  name:
    type: str
    required: true
    description: Project's name
  state:
    type: str
    description: Project's state
    default: present
    choices:
      - present
      - absent
  url:
    type: str
    description: Base URL for Semaphore API
    required: true
  token:
    type: str
    description: Authentication token for API
    required: true
"""
