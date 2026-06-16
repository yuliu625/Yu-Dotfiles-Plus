"""
Sources:
    https://github.com/yuliu625/Yu-LaTeX-Academic-Template/scripts/delete_gitkeep.py

References:
    None

Synopsis:
    自动删除 .gitkeep 文件的方法。

Notes:
    当前 template repository 为保证文件结果完整性，添加了大量 .gitkeep 文件进行占位。
    可以通过配置和运行当前脚本，删除相关占位符。

    当然，在绝大多数情况下， .gitkeep 并不会产生任何影响。可能的问题场景是:
        - 幽灵文件: 文件树会因此始终保持原始 template 定义。
        - 自动化: 少数情况会干扰自动化脚本运行。
        - 推送冲突: 不同的占位文件导致合并冲突。但日常 latex 合作基于第三方服务，不会产生该情况。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def remove_all_gitkeep(
    project_root_path: str | Path,
) -> None:
    project_root_path = Path(project_root_path)
    gitkeep_file_paths = list(project_root_path.glob('*.gitkeep'))
    for gitkeep_file_path in gitkeep_file_paths:
        gitkeep_file_path.unlink()


def smart_cleanup_gitkeep(
    project_root_path: str | Path,
) -> None:
    project_root_path = Path(project_root_path)
    gitkeep_file_paths = list(project_root_path.glob('*.gitkeep'))
    for gitkeep_file_path in gitkeep_file_paths:
        other_files = [
            file for file in gitkeep_file_path.parent.iterdir() if file.name != '.gitkeep'
        ]
        if len(other_files) > 0:
            gitkeep_file_path.unlink()


if __name__ == '__main__':
    pass

