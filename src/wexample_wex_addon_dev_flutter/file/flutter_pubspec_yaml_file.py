from __future__ import annotations

from wexample_filestate.item.file.yaml_file import YamlFile
from wexample_helpers.decorator.base_class import base_class


@base_class
class FlutterPubspecYamlFile(YamlFile):
    def get_dependencies_versions(
        self, optional: bool = False, group: str = "dev"
    ) -> dict[str, str]:
        config = self.read_config()

        dependencies = config.search(path="dependencies").get_dict_or_default(
            default={}
        )
        dev_dependencies = config.search(path="dev_dependencies").get_dict_or_default(
            default={}
        )

        merged = dict(dependencies)

        if group == "dev":
            merged.update(dev_dependencies)

        return merged

    def dumps(self, content: dict | None = None) -> str:
        workdir = self.get_parent_item()
        content["name"] = workdir.get_package_name()

        return super().dumps(content or {})
