from __future__ import absolute_import, division, print_function

MISSING_LIBRARY = None
MISSING_LIBRARY_E = None

try:
    import requests
except ImportError as e:
    MISSING_LIBRARY = "requests"
    MISSING_LIBRARY_E = e


from ansible.module_utils.basic import missing_required_lib


# pylint: disable=invalid-name
__metaclass__ = type


class SemaphoreComponent:

    # API attributes
    attrs = {"name": str}

    # Expected state of the component
    state = "present"

    # Base URL of Semaphore API
    __url: str

    # URL path for component
    path = ""

    # Auth token for API
    __token: str

    # Constructor
    def __init__(self, module):

        # Missing libraries
        if MISSING_LIBRARY:
            module.fail_json(
                msg=missing_required_lib(MISSING_LIBRARY), exception=MISSING_LIBRARY_E
            )

        # Save module
        self.module = module

        # Extract parameters
        self.__url = module.params.get("url")
        self.__token = module.params.get("token")
        self.state = module.params.get("state")

        # Extract attributes
        for key in self.attrs.keys():
            self.attrs[key] = module.params.get(key)

    # Get list of components from Semaphore
    def get_components(self):

        # Component URL
        url = self.__url + self.path

        # Workaround for inconsistency in Semaphore's API
        if self.path == '/project':
            url += 's'

        # Perform request
        try:
            ret = requests.get(url, headers={"Authorization": f"Bearer {self.__token}"})
        except requests.RequestException as e:
            self.module.fail_json(
                changed=False, msg=f"An error occured while performing the request: {e}"
            )

        # Check result
        if ret.status_code not in [200]:
            self.module.fail_json(
                changed=False,
                msg=f"Unexpected response code {ret.status_code} from server.",
                error=ret.text,
                url=str(url),
                path=self.path,
                method="GET"
            )

        # Read result
        try:
            components = ret.json()
        except requests.RequestException as e:
            self.module.fail_json(changed=False, msg=f"Cannot read returned JSON: {e}")

        # Return
        return components

    # Search for component in list
    def get_component(self, name):

        # Get list of existing components
        components = self.get_components()

        # Search by ID
        return next((x for x in components if x["name"] == name), None)

    # Create or update component
    def create_or_update(self):

        # Component URL
        url = self.__url + self.path

        # Check for existing component by name
        component = self.get_component(self.attrs["name"])

        # Catch requests exceptions
        try:

            # If component already exist, we try to update
            if component:

                # Check if changes happend
                changed = False
                for key, value in self.attrs.items():
                    if value != component[key]:
                        changed = True
                if not changed:
                    return self.module.exit_json(changed=False, result=component)

                # Prepare URL
                url = url + '/' + str(component["id"])

                # Prepare attributes
                self.attrs["id"] = component["id"]

                # Make PUT request
                ret = requests.put(
                    url,
                    json=self.attrs,
                    headers={"Authorization": f"Bearer {self.__token}"},
                )

                # Check result
                if ret.status_code not in [201, 204]:
                    self.module.fail_json(
                        changed=False,
                        msg=f"Unexpected response code {ret.status_code} from server.",
                        error=ret.text,
                        url=str(url),
                        attrs=self.attrs,
                        method="PUT"
                    )

                # Update component
                component = self.get_component(component["name"])

                # Return
                self.module.exit_json(changed=True, result=component)

            # If not, we create
            else:

                # Make POST request
                ret = requests.post(
                    url,
                    json=self.attrs,
                    headers={"Authorization": f"Bearer {self.__token}"},
                )

                # Check result
                if ret.status_code not in [201, 204]:
                    self.module.fail_json(
                        changed=False,
                        msg=f"Unexpected response code {ret.status_code} from server.",
                        error=ret.text,
                        url=str(url),
                        attrs=self.attrs,
                        method="POST"
                    )

                # Read result
                try:
                    component = ret.json()
                except requests.RequestException as e:
                    self.module.fail_json(
                        changed=False, msg=f"Cannot read returned JSON: {e}"
                    )

                # Return
                self.module.exit_json(changed=True, result=component)

        except requests.RequestException as e:
            self.module.fail_json(
                changed=False, msg=f"An error occured while performing the request: {e}"
            )

    # Ensure component does not exist
    def ensure_removed(self):

        # Check if component exists
        component = self.get_component(self.attrs["name"])
        if not component:
            return self.module.exit_json(changed=False)

        # Component URL
        url = self.__url + self.path + '/' + str(component["id"])

        # Catch requests exceptions
        try:

            # Make DELETE request
            ret = requests.delete(
                url, headers={"Authorization": f"Bearer {self.__token}"}
            )

            # Check result
            if ret.status_code not in [201, 204]:
                self.module.fail_json(
                    changed=False,
                    msg=f"Unexpected response code {ret.status_code} from server.",
                    error=ret.text,
                    url=str(url),
                    method="DELETE"
                )

            # Return
            self.module.exit_json(changed=True)

        except requests.RequestException as e:
            self.module.fail_json(
                changed=False, msg=f"An error occured while performing the request: {e}"
            )

    # Handle usage
    def handle(self):

        if self.state == "present":
            self.create_or_update()
        elif self.state == "absent":
            self.ensure_removed()
        else:
            self.module.fail_json(
                changed=False, msg=f"Invalid state requested: {self.state}"
            )


class SemaphoreProjectComponent(SemaphoreComponent):

    # API attributes
    attrs = SemaphoreComponent.attrs | {"project_id": int}

    # Constructor
    def __init__(self, module):
        super().__init__(module)

        # Update path
        self.path = f"/project/{self.attrs['project_id']}{self.path}"
