"""

"""

from pathlib import Path


def recursive_find_files_at_depth(
    root_dir: str,
    depth: int,
    file_names: list = None,
) -> list:
    root_dir = Path(root_dir)
    result = []
    for p in root_dir.rglob('*'):
        if p.is_file() and len(p.relative_to(root_dir).parts) == depth+1 and p.name in file_names:
            result.append(p)
    return result

