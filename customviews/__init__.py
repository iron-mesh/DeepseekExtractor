import os, sys, importlib
from dataclasses import dataclass, field

from PyUB.Types import Helper

__all__ = ["view_modules", "import_modules"]

view_modules = []
_custom_view_modules = {}

@dataclass
class ImportReport:
    is_success: bool = False
    trouble_modules: list[str] = field(default_factory=list)


def import_modules() -> ImportReport:
    global view_modules, _custom_view_modules
    helper = Helper()
    report = ImportReport()

    custom_view_modules_dir_path = os.path.dirname(__file__)
    view_pkg_path = helper.plugin_dir_abspath()

    sys.path.insert(0, custom_view_modules_dir_path)
    sys.path.insert(0, view_pkg_path)
    for entry in os.scandir(custom_view_modules_dir_path):
        if not (entry.is_file() and entry.name.endswith(".py") and entry.name != "__init__.py"):
            continue

        mod_name = entry.name[:-3]
        if mod_name in _custom_view_modules:
            try:
                importlib.reload(_custom_view_modules[mod_name])
            except Exception as e:
                del _custom_view_modules[mod_name]
                report.trouble_modules.append(mod_name)
        else:
            try:
                _custom_view_modules[mod_name] = importlib.import_module(mod_name)
            except Exception as e:
                report.trouble_modules.append(mod_name)
    sys.path.remove(custom_view_modules_dir_path)
    sys.path.remove(view_pkg_path)
    view_modules = list(_custom_view_modules.values())
    report.is_success = True if len(report.trouble_modules) == 0 else False
    return report

