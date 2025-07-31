"""
自动修改文件扩展名。
"""

from __future__ import annotations

import os
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def change_file_extensions(
    target_dir: str | Path,
    old_extension: str,
    new_extension: str,
):
    target_dir = Path(target_dir)

    for file_path in target_dir.iterdir():
        if file_path.is_file():
            if file_path.suffix == old_extension:
                new_file_path = file_path.with_suffix(new_extension)
                file_path.rename(new_file_path)


if __name__ == '__main__':
    target_dir_ = r""
    old_extension_ = ''
    new_extension_ = ''
    change_file_extensions(target_dir=target_dir_, old_extension=old_extension_, new_extension=new_extension_)

