from __future__ import absolute_import, division, print_function

# pylint: disable=invalid-name
__metaclass__ = type


class ModuleDocFragment:
    """
    Base options for every Semaphore component
    """

    DOCUMENTATION = r"""
options:
  type:
    type: str
    description: Type of template
    choices:
      - task
      - build
      - deploy
    default: task
  inventory_id:
    type: int
    required: true
    description: ID of inventory to use
  repository_id:
    type: int
    required: true
    description: ID of repository to use
  environment_id:
    type: int
    required: true
    description: ID of environment to use
  vault_key_id:
    type: int
    required: false
    description: ID of vault key to use
  view_id:
    type: int
    required: false
    description: ID of view to use
  playbook:
    type: str
    required: true
    description: Name of playbook file
  description:
    type: str
    required: false
    description: Task's description
  arguments:
    type: json
    required: false
    description: Task's extra arguments
    default: "[]"
  allow_override_args_in_task:
    type: bool
    required: false
    description: Allow override CLI args in task
    default: false
  suppress_success_alerts:
    type: bool
    required: false
    description: Suppress success alerts
    default: false
  survey_vars:
    type: list
    required: false
    description: Survey variables
    elements: dict
    suboptions:
      name:
        type: str
        description: Name
        required: true
      title:
        type: str
        description: Title
        required: true
      description:
        type: str
        description: Description
        required: false
      type:
        type: str
        description: Type
        required: false
        choices:
          - string
          - integer
      required:
        type: bool
        description: Required
        required: false
        default: false
"""
