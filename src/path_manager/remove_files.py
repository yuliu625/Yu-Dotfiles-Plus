"""
Sources:

References:

Synopsis:

Notes:
    危险方法！！！

    注意:
        - 确保对于备份文件进行操作！一定要有备份！
        - 这个方法仅用于传输至服务器时减轻压力。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def remove_files(
    root_dir: str | Path,
    pattern: str,
) -> None:
    root_dir = Path(root_dir)
    for file_path in root_dir.rglob(pattern):
        file_path.unlink()
        print(f"Deleted {file_path}")


if __name__ == '__main__':
    # 一定要检查是备份文件的路径！
    root_dir_ = r""  # 注意！一定要检查！
    pattern_ = r'*.db'

    remove_files(
        root_dir=root_dir_,
        pattern=pattern_,
    )

