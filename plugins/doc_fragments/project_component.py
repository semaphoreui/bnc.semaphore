from __future__ import absolute_import, division, print_function

# pylint: disable=invalid-name
__metaclass__ = type


class ModuleDocFragment:
    """
    Base options for project-dependant Semaphore component
    """

    DOCUMENTATION = r"""
options:
  project_id:
    type: int
    required: true
    description: Project's ID
"""
