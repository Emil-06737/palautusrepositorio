from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)

        name = parsed_content["tool"]["poetry"]["name"]
        description = parsed_content["tool"]["poetry"]["description"]
        dependencies = list(parsed_content["tool"]["poetry"]["dependencies"])
        dev_dependencies = list(parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"])
        license = parsed_content["tool"]["poetry"]["license"]
        authors = parsed_content["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
