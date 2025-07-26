"""
自动修改文件扩展名。
"""

from __future__ import annotations

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def change_file_extensions(
    target_dir: str | Path,
    old_extension: str,
    new_extensions: str,
):
    target_dir = Path(target_dir)

    for file_path in target_dir.iterdir():
        if file_path.is_file():
            if file_path.suffix == old_extension:
                new_file_path = file_path.with_suffix(new_extensions)
                file_path.rename(new_file_path)

