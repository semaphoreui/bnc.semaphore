from __future__ import absolute_import, division, print_function

from ansible_collections.bnc.semaphore.plugins.module_utils.component import (
    SemaphoreProjectComponent,
)


__metaclass__ = type


class SemaphoreTemplate(SemaphoreProjectComponent):

    # URL path for component
    # pylint: disable=unused-private-member
    path = "/templates"

    # Ansible module argument_spec
    argument_spec = SemaphoreProjectComponent.argument_spec | dict(
        type=dict(type="str", choices=["task", "build", "deploy"], default="task"),
        inventory_id=dict(type="int", required=True),
        repository_id=dict(type="int", required=True),
        environment_id=dict(type="int", required=True),
        vault_key_id=dict(type="int", required=False),
        view_id=dict(type="int", required=False),
        playbook=dict(type="str", required=True),
        description=dict(type="str", required=False),
        arguments=dict(type="json", required=False, default="[]"),
        allow_override_args_in_task=dict(type="bool", default=False),
        suppress_success_alerts=dict(type="bool", default=False),
        survey_vars=dict(
            type="list",
            required=False,
            elements="dict",
            options=dict(
                name=dict(type="str", required=True),
                title=dict(type="str", required=True),
                description=dict(type="str", required=False),
                type=dict(type="str", required=False, choices=["string", "integer"]),
                required=dict(type="bool", default=False),
            ),
        ),
    )


class SemaphoreTemplateTask(SemaphoreTemplate):

    # Ansible module argument_spec
    argument_spec = SemaphoreTemplate.argument_spec


class SemaphoreTemplateBuild(SemaphoreTemplate):

    # Ansible module argument_spec
    argument_spec = SemaphoreTemplate.argument_spec | dict(
        start_version=dict(type="str", required=True),
    )


class SemaphoreTemplateDeploy(SemaphoreTemplate):

    # Ansible module argument_spec
    argument_spec = SemaphoreTemplate.argument_spec | dict(
        build_template_id=dict(type="int", required=True),
        autorun=dict(type='bool', default=False)
    )
