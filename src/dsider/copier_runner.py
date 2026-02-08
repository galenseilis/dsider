from pathlib import Path

from copier import run_copy, run_update


def create_project(template_path, destination, answers=None):
    run_copy(
        src_path=template_path,
        dst_path=Path(destination),
        data=answers or {},
        overwrite=True,
    )


def update_project(project_path):
    run_update(Path(project_path))
