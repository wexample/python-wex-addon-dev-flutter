from __future__ import annotations

from wexample_wex_core.common.abstract_addon_manager import AbstractAddonManager


class FlutterAddonManager(AbstractAddonManager):
    def get_workdir_types(self) -> dict[str, type]:
        from wexample_wex_addon_dev_flutter.workdir.flutter_package_workdir import (
            FlutterPackageWorkdir,
        )
        from wexample_wex_addon_dev_flutter.workdir.flutter_packages_suite_workdir import (
            FlutterPackagesSuiteWorkdir,
        )
        from wexample_wex_addon_dev_flutter.workdir.flutter_workdir import (
            FlutterWorkdir,
        )

        return {
            "flutter": FlutterWorkdir,
            "flutter-package": FlutterPackageWorkdir,
            "flutter-packages-suite": FlutterPackagesSuiteWorkdir,
        }
