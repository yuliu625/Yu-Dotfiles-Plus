"""
Sources:

References:

Synopsis:
    文件树管理工具。

Notes:
    为简化文件树的管理，遵循约定大于配置。

    操作方法:
        - 全局配置。在项目根定义这个文件，所有路径相关均统一使用这个文件方法。
        - 指定 _BASE_DIR 。
        - 定义需要字段。使用 pydantic 定义所有的路径，类型全部是 Path 。
        - 定义文件树。在 get_file_tree 中写入所有的路径计算方法，基于 pathlib 实现。

    使用:
        - 约定。所有文件都默认使用 get_file_tree 方法获取路径。
        - 项目迁移。仅修改 _BASE_DIR 。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path
from pydantic import BaseModel, Field


__BASE_DIR = r""


class FileTree(BaseModel):
    """声明所有需要的路径。"""
    base_dir: Path = Field(
        description="最基础的路径，其他路径都由这个路径生成。",
    )


def get_file_tree(
    base_dir: str = __BASE_DIR,
) -> FileTree:
    """
    全局的获取文件树的方法。

    Args:
        base_dir (str, optional): 最根本的路径，其他路径都为其子路径。

    Returns:
        具体的所有子路径，都是 Path 对象。
    """
    base_dir = Path(base_dir)
    # 这里写生成FileTree的方法
    file_tree = FileTree(
        base_dir=base_dir,
    )
    return file_tree

