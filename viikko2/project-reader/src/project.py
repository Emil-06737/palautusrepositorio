class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors


    def _stringify_list(self, dependencies):
        return "\n- " + "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:{self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies:{self._stringify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:{self._stringify_list(self.dev_dependencies)}"
        )
